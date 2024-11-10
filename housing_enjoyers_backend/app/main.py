from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta, date
from model import LinearRegressionModel, KMeansModel
import pandas as pd
from Clustering import X as Data
from math import floor
from time import mktime


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
    t = mktime(target.timetuple())
    print("    Finding Date Function - Running:", index, array[index], t)
    if (array[index]['x'] == t):
        print("      returning index: ", index)
        return index # Lucky
    elif (after == False):
        print("      after == False")
        if ((index == 0) & (array[index]['x'] > t)):
            print("        returning index: ", index)
            return index # year is before our range
        elif (array[index - 1]['x'] < t < array[index]['x']):
            print("        returning index - 1: ", index - 1)
            return index - 1
        else:
            print("        returning above")
            return 'above'
    else:
        print("      after == True")
        if ((index == arraylen) & (array[index]['x'] < t)):
            print("        returning index: ", index)
            return index # year is after our range for some reason (we should be predicting)
        elif (array[index]['x'] < t < array[index + 1]['x']):
            print("        returning index + 1: ", index + 1)
            return index + 1
        else:
            print("        returning below")
            return 'below'
        
    return 'error' # Code should be unreachable



def binarySearch(array: list, target: date, after=False) -> int | bool:
    arraylen = len(array) - 1
    L: int = 0
    R: int = arraylen
    m: int = 0
    print("  initialised variables")

    print("  looping...")
    while L <= R:
        m = floor((L + R) / 2)
        print("    set midpoint:", m)
        res = foundDate(array, m, target, after, arraylen)
        print("    checked date: ", res)
        match (res):
            case 'above':
                L = m + 1
            case 'below':
                R = m - 1
            case _:
                return res
        print("    Loop Again - L: ", L, " R: ", R, " m: ", m)
    print("  loop ended returning False")
    
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
async def filteredlineardata(target_date_str):
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    year_start = date(target_date.year, 1, 1)
    year_end = date(target_date.year, 12, 31)

    try:
        print("predicting...")
        price_prediction = linear_model.predict()
        print("done")
        print("searching for start index...")
        start_index = binarySearch(price_prediction, year_start)
        print("done")
        print("searching for end index...")
        end_index = binarySearch(price_prediction, year_end, after=True)
        print("done")

        print("checking start and end indexes...")
        if (start_index == False or end_index == False):
            print("either start or end wasn't found")
            raise HTTPException(status_code=500, detail=str(e))
        print("done")

        result = []
        
        print("appending data to new list...")
        for i in range(start_index, end_index):
            result.append(price_prediction[i])
        print("done")

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
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    
    

    # ------------------------------------------------------------------------
    target_date_str = "2015-11-10"

    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    year_start = date(target_date.year, 1, 1)
    year_end = date(target_date.year, 12, 31)

    print("predicting...")
    price_prediction = linear_model.predict()
    print("done")
    print("searching for start index...")
    start_index = binarySearch(price_prediction, year_start)
    print("done")
    print("searching for end index...")
    end_index = binarySearch(price_prediction, year_end, after=True)
    print("done")

    print("checking start and end indexes...")
    if (start_index == False or end_index == False):
        print("  either start or end wasn't found")
        exit()
        # raise HTTPException(status_code=500, detail=str(e))
    print("done")

    result = []
    
    print("appending data to new list...")
    for i in range(start_index, end_index):
        result.append(price_prediction[i])
    print("done")
    print(result)
        
    # ------------------------------------------------------------------------
