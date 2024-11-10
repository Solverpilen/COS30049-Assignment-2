import pandas as pd
import datetime

pd.options.mode.use_inf_as_na = True

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw_Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned_Datasets/"

def date_to_int(row):
    string = row["Date"].split("/")
    date = datetime.datetime(int(string[2]), int(string[1]), int(string[0]), 0, 0, 0, 0)
    row["Date"] = date.timestamp()
    return row

df1 = pd.read_csv(CleanDataDirectory + 'Dataset1_Clean.csv')
df2 = pd.read_csv(CleanDataDirectory + 'Dataset2_Clean.csv')
df3 = pd.read_csv(CleanDataDirectory + 'Dataset3_Clean.csv')
df4 = pd.read_csv(CleanDataDirectory + 'Dataset4_Clean.csv')


combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

df_cleaned = combined_df.dropna()
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned = df_cleaned.drop(columns=["Unnamed: 0"])
df_cleaned = df_cleaned.apply(date_to_int, "columns")


df_cleaned.to_csv(
    CleanDataDirectory + "Dataset_Combined.csv", 
    sep=",",
    na_rep=""
)