from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
from pickle import load
from model import LinearRegressionModel, KMeansModel
import pandas as pd
from Clustering import X as Data

def affordability_category(house_price, borrowing_price):

    if  house_price <= borrowing_price/4:
        return 'high'
    elif borrowing_price/4 <= house_price <= borrowing_price:
        return 'medium'
    elif borrowing_price <= house_price <= borrowing_price + 300000:
        return 'low'
    else:
        return 'very low'
    
# setting up fast api and cors middleware

app = FastAPI()


origins = ["http://localhost:3000"]  


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 'data' is the pandas data frame used to process the raw data from the AI models
def pie_chart_ratings(borrowing_price,data):
    high = medium = low = very_low = 0

    # this allows the 'Price' column to be used as a parameter for affordabiility_category. It goes through all the prices in the data dataframe
    # and puts it through the function which then returns an array of ratings.
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

# obsolete function used for the second pie chart

def cluster_pie_chart_ratings(data):

    high, moderate, low = 0

    for rating in data['data']:
        if rating.Level == "High":
            high += 1
        elif rating.Level == "Moderate":
            moderate += 1
        elif rating.Level == "low":
            low += 1

    return high, moderate, low


class PricePredictionRequest(BaseModel):
    price_input: int


# POST request when a user inputs a borrowing price value which is stored in 'req'

@app.post("/price_prediction/{req}")

# function used to get a total amount of ratings for the pie chart, returns a dictionary of ratings, each with a corresponding number of each

async def price_prediction(req: int):
    try:
        high, medium, low, very_low = pie_chart_ratings(req, Data)
        return {'ratings': {'high': high, 'medium': medium, 'low': low, 'very_low': very_low}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# static GET request, is called each time the Affordability page is loaded
@app.get("/price_prediction/default_pie_chart")
async def default_pie_chart():

    data = Data

    # default borrowing price, based on the data from the Australian Beureau of Statistics, data is referenced in the report
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
    
# Pass trained data from clustering model backend to frontend 
@app.get("/models/ClusterModel") 
async def clusterdata():
    try:
        cluster_prediction = kmeans_model.predict()

        high, moderate, low = cluster_pie_chart_ratings(cluster_prediction)

        return { 'ratings': { 'high': high, 'moderate' : moderate, 'low': low }}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Initiate Backend Server 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
