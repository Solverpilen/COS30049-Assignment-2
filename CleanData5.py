import pandas as pd

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"

Data5 = pd.read_csv(RawDataDirectory + "Melbourne_housing.csv")

Data5.dropna()
Data5 = Data5.drop_duplicates()