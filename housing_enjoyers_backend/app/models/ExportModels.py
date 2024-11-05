import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

pd.options.mode.use_inf_as_na = True

CleanDataDirectory = "COS30049-Assignment-2/COS30049-Assignment-2/housing_enjoyers_backend/app/models/Cleaned_Datasets/"

Data = pd.read_csv("COS30049-Assignment-2\\housing_enjoyers_backend\\app\\models\\Cleaned_Datasets\\Dataset_Combined.csv", 
                   dtype={
                        "Suburb": "string",
                        "Rooms": "Int32",
                        "Type": "string",
                        "Date": "Int32",
                        "Distance": "float",
                        "Postcode": "string",
                        "Bedroom": "Int32",
                        "Bathroom": "Int32",
                        "Car": "Int32",
                        "Landsize": "Int32",
                        "Latitude": "float",
                        "Longtitude": "float",
                        "ParkingArea": "string",
                        "Price": "Int32"
                        })

X = Data[['Date']]  
y = Data['Price']  

model = LinearRegression()
model.fit(X, y)

filehandler = open("COS30049-Assignment-2\\housing_enjoyers_backend\\app\\LinearRegModel.sav", "wb")

pickle.dump(model, filehandler)


model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

filehandler = open("COS30049-Assignment-2\\housing_enjoyers_backend\\app\\ClusterModel.sav", "wb")

pickle.dump(model, filehandler)