import pandas as pd

# Load dataset
file_path = "COS30049-Assignment-2\Raw Datasets\house-prices-by-small-area-sale-year.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = "COS30049-Assignment-2\Raw Datasets\MELBOURNE_HOUSE_PRICES_LESS.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = "COS30049-Assignment-2\Raw Datasets\Melbourne_housing_FULL_acedit.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = "COS30049-Assignment-2\Raw Datasets\Melbourne_housing_FULL.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = "COS30049-Assignment-2\Raw Datasets\Melbourne_housing.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)