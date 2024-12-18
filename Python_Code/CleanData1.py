import pandas as pd


pd.options.mode.use_inf_as_na = True

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"


Data1Raw = pd.read_csv(RawDataDirectory + "MELBOURNE_HOUSE_PRICES_LESS.csv", 
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
                        "RegionName": "string",
                        "PropertyCount": "Int32",
                        "Distance": "float",
                        "CouncilArea": "string"
                        }
                    )


Data1Raw = Data1Raw.drop(columns=["Address", "Method", "SellerG", "CouncilArea"])

Data1Raw = Data1Raw.dropna()

Data1Raw = Data1Raw.drop_duplicates()
Data1Raw = Data1Raw.reindex(
    [
        "Date",
        "Suburb",
        "Postcode",
        "Distance",
        "Type",
        "Rooms",
        "Price"
    ], 
    axis=1
    )

Data1Raw.to_csv(
    CleanDataDirectory + "Dataset1_Clean.csv", 
    sep=",",
    na_rep=""
    )

DataCleaned = pd.read_csv(CleanDataDirectory + "Dataset1_Clean.csv", 
                    dtype={
                        "Suburb": "string",
                        "Rooms": "Int32",
                        "Type": "string",
                        "Price": "Int32",
                        "Date": "string",
                        "Postcode": "string",
                        "Distance": "float"
                        }
                    )
