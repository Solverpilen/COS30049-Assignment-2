# Libraries
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks, Depends
from pickle import load
# Local Files
from models.ModelInputs import ModelInputs
from models.Clustering import X_Bedroom, color_map, affordability_category
from fastapi.middleware.cors import CORSMiddleware

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

# @app.post("/price_prediction/{price_input}")
# async def price_prediction(price_input : ModelInputs):
        

#      pass

# @app.get("/price_prediction/")
# def priceGraph():
#     pass

@app.get("/price_prediction/default_pie_chart")
async def default_pie_chart():

    borrowing_price = 394300

    high, medium, low, very_low = pie_chart_ratings(borrowing_price)

    return { 'ratings': {'high': high, 'medium': medium, 'low': low, 'very low': very_low } }


