import pandas as pd

CleanDataDirectory = './models/Cleaned_Datasets/'

Data = pd.read_csv(CleanDataDirectory + "Dataset_Combined.csv", 
                   dtype={
                        "Suburb": "string",
                        "Rooms": "Int32",
                        "Type": "string",
                        "Date": "string",
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

X = Data[['Price', 'Bathroom']].dropna()  
X_Bedroom = Data[['Price', 'Bedroom']].dropna()

def affordability_category(house_price, borrowing_price):
    if  house_price <= borrowing_price/4:
        return 'high'
    elif borrowing_price/4 <= house_price <= borrowing_price:
        return 'medium'
    elif borrowing_price <= house_price <= borrowing_price + 300000:
        return 'low'
    else:
        return 'very low'