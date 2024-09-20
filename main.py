import pandas as pd

df = pd.read_csv('house-prices-by-small-area-sale-year.csv')

df_cleaned = df.dropna()


