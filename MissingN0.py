import pandas as pd

working_directory = "COS30049-Assignment-2/Raw Datasets/"

# Load dataset
file_path = working_directory + "house-prices-by-small-area-sale-year.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = working_directory + "MELBOURNE_HOUSE_PRICES_LESS.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = working_directory + "Melbourne_housing_FULL_acedit.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = working_directory + "Melbourne_housing_FULL.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)

# Load dataset
file_path = working_directory + "Melbourne_housing.csv"
sales_data = pd.read_csv(file_path)

# identifying the missing data
missing_values = sales_data.isnull().sum()

print("\n\n" + file_path + "\n")
print(missing_values)