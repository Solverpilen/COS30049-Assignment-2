from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from pickle import load
import os
import pandas as pd

<<<<<<< HEAD
from models.ModelInputs import ModelInputs
from models.Clustering import X_Bedroom, Data, affordability_category, X
=======
from models.ModelInputs import ModelInputs, PricePredictionRequest
from models.Clustering import X_Bedroom, color_map, affordability_category
>>>>>>> c29e63cf89f5838b3e64b78eb6c854ad2f9c6883


app = FastAPI()


origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


linearRegModel = load(open("LinearRegModel.sav", "rb"))
clusteringModel = load(open("ClusterModel.sav", "rb"))


def affordability_chart_ratings(borrowing_price, data):
    high = medium = low = very_low = 0
    ratings = data['Price'].apply(lambda price: affordability_category(price, borrowing_price))

    for r in ratings:
        match r:
            case 'high':
                high += 1
            case 'medium':
                medium += 1
            case 'low':
                low += 1
            case 'very low':
                very_low += 1

    return high, medium, low, very_low

<<<<<<< HEAD
class PricePredictionRequest(BaseModel):
    price_input: int

=======
>>>>>>> c29e63cf89f5838b3e64b78eb6c854ad2f9c6883



@app.post("/price_prediction/{req}")
async def price_prediction(req: int):
    try:
        high, medium, low, very_low = affordability_chart_ratings(req)
        return {'ratings': {'high': high, 'medium': medium, 'low': low, 'very low': very_low}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/price_prediction/default_pie_chart")
async def default_pie_chart():
    borrowing_price = 394300  
    high, medium, low, very_low = affordability_chart_ratings(borrowing_price, Data)
    return {'ratings': {'high': high, 'medium': medium, 'low': low, 'very low': very_low}}


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

    
    return total_ratings


        










@app.get("/housing_data/{target_date}")
async def get_housing_data(target_date: str):
    try:
        data = get_filtered_data("data/housing_prices.csv", target_date)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
