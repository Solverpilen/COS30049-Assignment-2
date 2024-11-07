from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from pickle import load
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

from models.Clustering import X_Bedroom, Data, X
from models.ModelInputs import ModelInputs, PricePredictionRequest

from utils.ClusteringFunctions import affordability_chart_ratings


linearRegModel: LinearRegression = load(open("LinearRegModel.sav", "rb"))
clusteringModel: KMeans = load(open("ClusterModel.sav", "rb"))


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/price_prediction/{req}")
async def price_prediction(req: int):
    try:
        high, medium, low, very_low = affordability_chart_ratings(req)
        # ----- Test -----
        print(req)
        print(high)
        print(medium)
        print(low)
        print(very_low)
        # ----- Test -----
        return {'ratings': {'high': high, 'medium': medium, 'low': low, 'very low': very_low}}
    except Exception as e:
        # ----- Test -----
        print(e)
        # ----- Test -----
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/price_prediction/default_pie_chart")
async def default_pie_chart():
    borrowing_price = 394300  
    high, medium, low, very_low = affordability_chart_ratings(borrowing_price, Data)
    return {'ratings': {'high': high, 'medium': medium, 'low': low, 'very low': very_low}}


@app.get("/price_prediction/default_bar_chart")
async def default_bar_chart():

    borrowing_price = 394300  
    total_ratings = {}

    for i in range(1, 5):

        bedroom = X_Bedroom.loc[X_Bedroom['Bedroom'] == i]

        high, medium, low, very_low = affordability_chart_ratings(borrowing_price, bedroom)

        total_ratings[str(i) + "_bedroom_ratings"] = {"high": high, "medium" : medium, "low" : low, "very low": very_low}

    
    for i in range (1, 5):

        bathroom = X.loc[X['Bathroom'] == i]

        high, medium, low, very_low = affordability_chart_ratings(borrowing_price, bathroom)

        total_ratings[str(i) + "_bathroom_ratings"] = {"high": high, "medium" : medium, "low" : low, "very low": very_low}

    # 1 loop attempt
    # for i in range(1, 5):

    #     bedroom = X_Bedroom.loc[X_Bedroom['Bedroom'] == i]
    #     high, medium, low, very_low = affordability_chart_ratings(borrowing_price, bedroom)
    #     total_ratings[str(i) + "_bedroom_ratings"] = {"high": high, "medium" : medium, "low" : low, "very low": very_low}

    #     bathroom = X.loc[X['Bathroom'] == i]
    #     high, medium, low, very_low = affordability_chart_ratings(borrowing_price, bathroom)
    #     total_ratings[str(i) + "_bathroom_ratings"] = {"high": high, "medium" : medium, "low" : low, "very low": very_low}

    
    return total_ratings


# ----- Does the below actually get used? ----------------------------------------------------------
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
# --------------------------------------------------------------------------------------------------