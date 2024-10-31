# Libraries
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks, Depends
from pickle import load
# Local Files
from models.ModelInputs import ModelInputs
from models.Clustering import X_Bedroom, color_map

app = FastAPI()

linearRegModel = load(open("LinearRegModel.sav", "rb"))



# HTTP Requests

@app.post("/price_prediction/{price_input}")
def pricePred(price_input : ModelInputs):

    pass

@app.get("/price_prediction/")
def priceGraph():
    pass

@app.get("/price_prediction/defualt_pie_chart")
async def default_pie_chart():

    high: int
    medium: int
    low: int
    very_low: int

    ratings = X_Bedroom['affordability']

    for rating in ratings:
        if(rating == 'high'):
            high += 1
        elif(rating == 'medium'):
            medium += 1
        elif(rating == 'low'):
            low += 1
        elif(rating == 'very low'):
            very_low += 1

    ratings = { high, medium, low, very_low}


    return {"ratings" : ratings, "Color Map": color_map }


