# Libraries
import os
import pandas as pd
from datetime import datetime, timedelta
from pickle import load
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
# Local Files
from models.Clustering import X_Bedroom, Data, X
from models.ModelInputs import ModelInputs, PricePredictionRequest
from utils.ClusteringFunctions import affordability_chart_ratings_old, affordability_chart_ratings_new


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
    print("Predicting Prices")
    try:
        high, medium, low, very_low = affordability_chart_ratings_new(req, Data)
        # ----- Test -----
        print(req)
        print(high)
        print(medium)
        print(low)
        print(very_low)
        # ----- Test -----
        return {"ratings": {high, medium, low, very_low}}
    except Exception as e:
        # ----- Test -----
        print(e)
        # ----- Test -----
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/price_prediction/default_pie_chart")
async def default_pie_chart():
    print("Default Pie Chart Loading - fake predict")
    borrowing_price = 394300  
    # high, medium, low, very_low = affordability_chart_ratings_new(borrowing_price, Data)
    # return {"ratings": {high, medium, low, very_low}}
    return price_prediction(borrowing_price)


@app.get("/price_prediction/default_bar_chart")
async def default_bar_chart():

    borrowing_price = 394300
    total_ratings = {}

    # for i in range(1, 5):

    #     bedroom = X_Bedroom.loc[X_Bedroom["Bedroom"] == i]

    #     high, medium, low, very_low = affordability_chart_ratings_new(borrowing_price, bedroom)

    #     total_ratings[str(i) + "_bedroom_ratings"] = {"high": high, "medium" : medium, "low" : low, "very_low": very_low}

    
    # for i in range (1, 5):

    #     bathroom = X.loc[X["Bathroom"] == i]

    #     high, medium, low, very_low = affordability_chart_ratings_new(borrowing_price, bathroom)

    #     total_ratings[str(i) + "_bathroom_ratings"] = {"high": high, "medium" : medium, "low" : low, "very_low": very_low}

    # 1 loop attempt
    for i in range(1, 5):

        bedroom = X_Bedroom.loc[X_Bedroom["Bedroom"] == i]
        high, medium, low, very_low = affordability_chart_ratings_new(borrowing_price, bedroom)
        total_ratings[str(i) + "_bedroom_ratings"] = {high, medium, low, very_low}

        bathroom = X.loc[X["Bathroom"] == i]
        high, medium, low, very_low = affordability_chart_ratings_new(borrowing_price, bathroom)
        total_ratings[str(i) + "_bathroom_ratings"] = {high, medium, low, very_low}

    
    return total_ratings


# ----- Does the below actually get used? ----------------------------------------------------------
def get_filtered_data(file_path, target_date_str):
    print("Getting Filtered Data")
    try:
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        
        df = pd.read_csv(file_path, parse_dates=["Date"])
        
        start_date = target_date - timedelta(days=7)
        end_date = target_date + timedelta(days=7)
        
        filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
        
        return filtered_df.to_dict(orient="records")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {e}")


@app.get("/housing_data/{target_date}")
async def get_housing_data(target_date: str):
    print("Getting Housing Data")
    try:
        data = get_filtered_data("data/housing_prices.csv", target_date)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# --------------------------------------------------------------------------------------------------