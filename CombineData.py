import pandas as pd

pd.options.mode.use_inf_as_na = True

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"

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

#print(combined_df)

df_cleaned.to_csv(
    CleanDataDirectory + "Dataset_Combined.csv", 
    sep=",",
    na_rep=""
    )