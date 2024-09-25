import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.mode.use_inf_as_na = True

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"

Data = pd.read_csv(CleanDataDirectory + "Dataset_Combined.csv", 
                    dtype={
                        "Suburb": "string",
                        "Rooms": "Int32",
                        "Type": "string",
                        "Date": "string",
                        "Distance": "float",
                        "Postcode": "string",
                        "Bedroom": "Int32",
                        "Bathroom": "Int32",
                        "Car": "Int32",
                        "Landsize": "Int32",
                        "Latitude": "float",
                        "Longtitude": "float",
                        "ParkingArea": "string",
                        "Price": "Int32"
                        }
                    )

plt.figure(figsize=(10, 8))
corr_matrix = Data.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

plt.figure(figsize=(10, 8))
plt.scatter(Data['Rooms'], Data['Price'], alpha=0.6, color='b')
plt.title('Scatter Plot of Average Rooms vs. House Price')
plt.xlabel('Average Number of Rooms per Household (AveRooms)')
plt.ylabel('House Price (in $100,000)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 8))
plt.plot("Date", "Price", Data)
