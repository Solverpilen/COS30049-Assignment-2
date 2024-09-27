from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

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
                        })


X = Data[['Price', 'Bathroom']].dropna()  

# Plot original data
plt.figure(figsize=(12, 6))
plt.scatter(X['Price'], X['Bathroom'], c='blue')
plt.title('Original Housing Data')
plt.xlabel('Price')
plt.ylabel('Bathroom')
plt.grid(True)
plt.show()


model = KMeans(n_clusters=3, random_state=42)
model.fit(X)


all_predictions = model.predict(X)


plt.figure(figsize=(12, 6))
plt.scatter(X['Price'], X['Bathroom'], c=all_predictions, cmap='viridis')
plt.title('K-Means Clustering: Price vs Bathroom')
plt.xlabel('Price')
plt.ylabel('Bathroom')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()


predicted_label = model.predict([[1500000, 2]])  
print(f'The predicted cluster for the sample [Price: 1500000, Bathroom: 2] is: {predicted_label[0]}')
