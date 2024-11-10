from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta, date
from pickle import load
from model import LinearRegressionModel, KMeansModel
import pandas as pd
from Clustering import X as Data
from math import floor


def affordability_category(house_price, borrowing_price):
    if  house_price <= borrowing_price/4:
        return 'high'
    elif borrowing_price/4 <= house_price <= borrowing_price:
        return 'medium'
    elif borrowing_price <= house_price <= borrowing_price + 300000:
        return 'low'
    else:
        return 'very low'
app = FastAPI()


origins = ["http://localhost:3000"]  


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def pie_chart_ratings(borrowing_price,data):
    high = medium = low = very_low = 0
    ratings = data['Price'].apply(lambda price: affordability_category(price, borrowing_price))

    for rating in ratings:
        if rating == 'high':
            high += 1
        elif rating == 'medium':
            medium += 1
        elif rating == 'low':
            low += 1
        elif rating == 'very low':
            very_low += 1

    return high, medium, low, very_low


class PricePredictionRequest(BaseModel):
    price_input: int




@app.post("/price_prediction/{req}")
async def price_prediction(req: int):
    try:
        high, medium, low, very_low = pie_chart_ratings(req, Data)
        return {'ratings': {'high': high, 'medium': medium, 'low': low, 'very_low': very_low}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/price_prediction/default_pie_chart")
async def default_pie_chart():

    data = Data
    borrowing_price = 394300  
    high, medium, low, very_low = pie_chart_ratings(borrowing_price, data)
    return {'ratings': {'high': high, 'medium': medium, 'low': low, 'very_low': very_low}}


def get_filtered_data(file_path, target_date_str):
    try:
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        
        df = pd.read_csv(file_path, parse_dates=['Date'])
        
        start_date = target_date - timedelta(days=7)
        end_date = target_date + timedelta(days=7)
        
        
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        return filtered_df.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {e}")


@app.get("/housing_data/{target_date}")
async def get_housing_data(target_date: str):
    try:
        data = get_filtered_data("data/housing_prices.csv", target_date)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def foundDate(array: list, index: int, target: date, after: bool, arraylen: int) -> int | str :
    if (array[index]['x'] == target):
        return index # Lucky
    elif (after == False):
        if (index == 0 & array[index]['x'] > target):
            return index # year is before our range
        elif (array[index - 1]['x'] < target < array[index]['x']):
            return index - 1
        else:
            return 'above'
    else:
        if (index == arraylen & array[index]['x'] < target):
            return index # year is after our range for some reason (we should be predicting)
        elif (array[index]['x'] < target < array[index + 1]['x']):
            return index + 1
        else:
            return 'below'



def binarySearch(array: list, target: date, after=False) -> int | False:
    arraylen = len(array)
    L: int = 0
    R: int = arraylen
    m: int = 0

    while L <= R:
        m = floor((L + R) / 2)
        res = foundDate(array, m, target, after, arraylen)
        match (res):
            case 'above':
                L = m + 1
            case 'below':
                R = m - 1
            case _:
                return res
    
    return False


linear_model = LinearRegressionModel()
kmeans_model = KMeansModel()



# Pass trained data from linear model backend to frontend 
@app.get("/models/LinearRegModel") 
async def lineardata():
    try:
        price_prediction = linear_model.predict()
        return {'data': price_prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Pass trained data from linear model backend to frontend within a date range
@app.get("/models/LinearRegModel/{target_date_str}") 
async def lineardata(target_date_str):
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    year_start = date(target_date.year, 1, 1)
    year_end = date(target_date.year, 12, 31)

    try:
        price_prediction = linear_model.predict()
        start_index = binarySearch(price_prediction, year_start)
        end_index = binarySearch(price_prediction, year_end, after=True)

        if (start_index == False or end_index == False):
            raise HTTPException(status_code=500, detail=str(e))
        
        result = []
        
        for i in range(start_index, end_index):
            result.append(price_prediction[i])

        return {'data': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Pass trained data from clustering model backend to frontend 
@app.get("/models/ClusterModel") 
async def clusterdata():
    try:
        cluster_prediction = kmeans_model.predict()

        return {"data": cluster_prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Initiate Backend Server 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
