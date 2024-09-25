import pandas as pd

pd.options.mode.use_inf_as_na = True

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"

"""
Some Key Details
Suburb: Suburb

Rooms: Number of rooms

Price: Price in Australian dollars

Type:
br - bedroom(s);
h - house, cottage, villa, semi, terrace;
u - unit, duplex;
t - townhouse;
dev site - development site;
o res - other residential.

Date: Date sold

Distance: Distance from CBD in Kilometres

Bedroom2 : Scraped # of Bedrooms (from different source)

Bathroom: Number of Bathrooms

Car: Number of carspots

Landsize: Land Size in Metres

Lattitude: Self explanitory

Longtitude: Self explanitory
"""

Data4Raw = pd.read_csv(RawDataDirectory + "Melbourne_housing.csv", 
                    dtype={
                        "Suburb": "string",
                        "Address": "string",
                        "Rooms": "Int32",
                        "Type": "string",
                        "Method": "string",
                        "SellerG": "string",
                        "Date": "string",
                        "Distance": "float",
                        "Postcode": "string",
                        "Bedroom": "Int32",
                        "Bathroom": "Int32",
                        "Car": "Int32",
                        "Landsize": "Int32",
                        "BuildingArea": "string",
                        "YearBuilt": "Int32",
                        "CouncilArea": "string",
                        "Latitude": "float",
                        "Longtitude": "float",
                        "Regionname": "string",
                        "Propertycount": "Int32",
                        "ParkingArea": "string",
                        "Price": "Int32"
                        }
                    )

missing_values = Data4Raw.isnull().sum()
print(missing_values)

Data4Raw = Data4Raw.drop(columns=["Address", "Method", "SellerG", "BuildingArea", "Regionname", "YearBuilt", "Propertycount", "CouncilArea", "ParkingArea"])
Data4Raw = Data4Raw.dropna()
Data4Raw = Data4Raw.drop_duplicates()
Data4Raw = Data4Raw.reindex(
    [
        "Date",
        "Suburb",
        "Postcode",
        "Latitude",
        "Longtitude",
        "Distance",
        "Type",
        "Rooms",
        "Bedroom",
        "Bathroom",
        "Car",
        "Landsize",
        "Price"
    ], 
    axis=1
    )

Data4Raw.to_csv(
    CleanDataDirectory + "Dataset4_Clean.csv", 
    sep=",",
    na_rep=""
    )

Data5 = pd.read_csv(CleanDataDirectory + "Dataset4_Clean.csv", 
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
                        "Price": "Int32"
                        }
                    )
