import pandas as pd

df1 = pd.read_csv('house-prices-by-small-area-sale-year.csv')
df2 = pd.read_csv('MELBOURNE_HOUSE_PRICES_LESS.csv')
df3 = pd.read_csv('Melbourne_housing_FULL_acedit.csv')
df4 = pd.read_csv('Melbourne_housing_FULL.csv')
df5 = pd.read_csv('Melbourne_housing.csv')

columns = ['suburb', 'rooms', 'type', 'date', 'price']

df1 = df1[columns]
df2 = df2[columns]
df3 = df3[columns]
df4 = df4[columns]
df5 = df5[columns]

combined_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

df_cleaned = combined_df.dropna()

print(combined_df)

