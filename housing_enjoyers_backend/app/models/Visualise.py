import pandas as pd

pd.options.mode.use_inf_as_na = True

RawDataDirectory = "Raw_Datasets/"
CleanDataDirectory = "Cleaned_Datasets/"

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
                        }
                    )