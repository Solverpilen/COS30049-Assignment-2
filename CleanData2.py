import pandas as pd


pd.options.mode.use_inf_as_na = True

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"


DataRaw = pd.read_csv(RawDataDirectory + "MELBOURNE_HOUSE_PRICES_LESS.csv", 
                    dtype={
                        "Suburb": "string",
                        "Address": "string",
                        "Rooms": "Int32",
                        "Type": "string",
                        "Price": "Int32",
                        "Method": "string",
                        "SellerG": "string",
                        "Date": "string",
                        "Postcode": "string",
                        "Regionname": "string",
                        "Propertycount": "Int32",
                        "Distance": "float",
                        "CouncilArea": "string"
                        }
                    )


DataRaw = DataRaw.drop(columns=["Address", "Method", "SellerG", "CouncilArea"])

DataRaw = DataRaw.dropna()

DataRaw = DataRaw.drop_duplicates()

DataRaw.to_csv(
    CleanDataDirectory + "New_Dataset_Clean.csv", 
    sep=",",
    na_rep=""
    )

DataCleaned = pd.read_csv(CleanDataDirectory + "New_Dataset_Clean.csv", 
                    dtype={
                        "Suburb": "string",
                        "Rooms": "Int32",
                        "Type": "string",
                        "Price": "Int32",
                        "Date": "string",
                        "Postcode": "string",
                        "Regionname": "string",
                        "Propertycount": "Int32",
                        "Distance": "float"
                        }
                    )