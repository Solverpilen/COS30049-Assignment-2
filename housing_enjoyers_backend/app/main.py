# Libraries
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks, Depends
from pickle import load
# Local Files
from models.ModelInputs import ModelInputs

app = FastAPI()

linearRegModel = load(open("LinearRegModel.sav", "rb"))



# HTTP Requests

@app.post("/price_prediction")
def pricePred(input : ModelInputs):
    pass

@app.get("/price_prediction/")
def priceGraph():
    pass