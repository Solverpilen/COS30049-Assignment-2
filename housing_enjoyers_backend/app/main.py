from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, date
from model import LinearRegressionModel, KMeansModel
from utils.Clustering import X as Data
from utils.PieChartFunctions import pie_chart_ratings, cluster_pie_chart_ratings
from utils.LineChartFunctions import binarySearch
    
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


# POST request when a user inputs a borrowing price value which is stored in 'req'
# function used to get a total amount of ratings for the pie chart, returns a dictionary of ratings, each with a corresponding number of each
@app.post("/price_prediction/{req}")
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

        high, moderate, low = cluster_pie_chart_ratings(cluster_prediction)

        return { 'ratings': { 'high': high, 'moderate' : moderate, 'low': low }}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Initiate Backend Server 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)