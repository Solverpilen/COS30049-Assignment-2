import pandas as pd
import datetime

pd.options.mode.use_inf_as_na = True

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"

def date_to_int(row):
    string = row["Date"].split("/")
    # string = string[2] + "" + string[1] + "" + string[0]
    date = datetime.datetime(int(string[2]), int(string[1]), int(string[0]), 0, 0, 0, 0)
    # row["Date"] = int(string)
    row["Date"] = date.timestamp()
    return row

df1 = pd.read_csv(CleanDataDirectory + 'Dataset1_Clean.csv')
df2 = pd.read_csv(CleanDataDirectory + 'Dataset2_Clean.csv')
df3 = pd.read_csv(CleanDataDirectory + 'Dataset3_Clean.csv')
df4 = pd.read_csv(CleanDataDirectory + 'Dataset4_Clean.csv')

# columns = ['Suburb', 'Rooms', 'Type', 'Date', 'Price']

# the common columns for each data set is Suburb, rooms, type, price, rooms
# df1 = df1[columns]
# df2 = df2[columns]
# df3 = df3[columns]
# df4 = df4[columns]

combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

df_cleaned = combined_df.dropna()
df_cleaned = df_cleaned.drop_duplicates()
df_cleaned = df_cleaned.apply(date_to_int, "columns")

# for row in df_cleaned["Date"]:
#     string = row.split("/")
#     string = string[2] + "" + string[1] + "" + string[0]
#     # date = datetime.date.fromisoformat(string)
#     row = int(string)

df_cleaned.to_csv(
    CleanDataDirectory + "Dataset_Combined.csv", 
    sep=",",
    na_rep=""
    )