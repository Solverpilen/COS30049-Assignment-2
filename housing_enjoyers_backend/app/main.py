# Libraries
import pandas as pd
from datetime import datetime, timedelta
from pickle import load
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
# Local Files
from models.Clustering import X_Bedroom, affordability_category, Data, X
from models.ModelInputs import ModelInputs, PricePredictionRequest
from utils.ClusteringFunctions import affordability_chart_ratings_old, affordability_chart_ratings_new


linearRegModel: LinearRegression = load(open("LinearRegModel.sav", "rb"))
clusteringModel: KMeans = load(open("ClusterModel.sav", "rb"))


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # URL of React application
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


linearRegModel = load(open("LinearRegModel.sav", "rb"))

def pie_chart_ratings(borrowing_price):

    high = 0
    medium = 0
    low = 0
    very_low = 0

    ratings = X_Bedroom['Price'].apply(lambda price: affordability_category(price, borrowing_price))

    for rating in ratings:
        if(rating == 'high'):
            high += 1
        elif(rating == 'medium'):
            medium += 1
        elif(rating == 'low'):
            low += 1
        elif(rating == 'very low'):
            very_low += 1

            
    return high, medium, low, very_low


# HTTP Requests

@app.post("/price_prediction/{price_input}")
async def price_prediction(price_input : int):


    high, medium, low, very_low = pie_chart_ratings(price_input)

    return { 'ratings': {'high': high, 'medium': medium, 'low': low, 'very low': very_low } }        

#      pass

# @app.get("/price_prediction/")
# def priceGraph():
#     pass

@app.get("/price_prediction/default_pie_chart")
async def default_pie_chart():

    borrowing_price = 394300

    high, medium, low, very_low = pie_chart_ratings(borrowing_price)

    return { 'ratings': {'high': high, 'medium': medium, 'low': low, 'very low': very_low } }
