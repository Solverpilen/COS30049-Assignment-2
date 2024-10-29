import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

pd.options.mode.use_inf_as_na = True

CleanDataDirectory = "COS30049-Assignment-2/Cleaned_Datasets/"

Data = pd.read_csv(CleanDataDirectory + "Dataset_Combined.csv", 
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

filehandler = open("COS30049-Assignment-2\housing_enjoyers_backend\app\LinearRegModel.sav", "wb")

pickle.dump(model, filehandler)