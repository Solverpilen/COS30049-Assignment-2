import pandas as pd

# Load dataset
file_path = "./Raw Datasets/house-prices-by-small-area-sale-year.csv.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print(missing_values)