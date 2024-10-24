from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score

pd.options.mode.use_inf_as_na = True

WorkingDirectory = '/COS30049-Assignment-2/'
RawDataDirectory =  WorkingDirectory + 'Raw_Datasets/'
CleanDataDirectory = WorkingDirectory + 'Cleaned_Datasets/'

def affordability_category(price):
    if price <= 100000:
        return 'high'
    elif 100001 <= price <= 362400:
        return 'medium'
    elif 362401 <= price <= 800000:
        return 'low'
    else:
        return 'very low'

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
X_Bedroom = Data[['Price', 'Bedroom']].dropna()

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

X_Bedroom['affordability'] = X_Bedroom['Price'].apply(affordability_category)

#model_bedroom = KMeans(n_clusters=4, random_state=42)
#model_bedroom.fit(X_Bedroom)

#bedroom_predictions = model_bedroom.predict(X_Bedroom)

color_map = {'very low': 'red', 'low': 'orange', 'medium': 'green', 'high': 'blue'}

plt.figure(figsize=(12, 6))
plt.scatter(X['Price'], X['Bathroom'], c=all_predictions, cmap='viridis')
plt.title('K-Means Clustering: Price vs Bathroom')
plt.xlabel('Price')
plt.ylabel('Bathroom')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(X_Bedroom['Price'], X_Bedroom['Bedroom'], c=X_Bedroom['affordability'].map(color_map), s=100, alpha=0.6)
plt.title('Housing Prices and Bedrooms - Clustered')
plt.xlabel('Bedrooms')
plt.ylabel('Price ($)')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()

#plt.figure(figsize=(12, 6))
#plt.scatter(X_Bedroom['Price'], X_Bedroom['Bedroom'], c=bedroom_predictions, cmap='viridis')
#plt.title('K-Means Clustering: Price vs Bedroom')
#plt.xlabel('Price')
#plt.ylabel('Bedroom')
#plt.colorbar(label='Cluster')
#plt.grid(True)
#plt.show()


predicted_label = model.predict([[1500000, 2]])  
print(f'The predicted cluster for the sample [Price: 1500000, Bathroom: 2] is: {predicted_label[0]}')

silhouette_avg_bathroom = silhouette_score(X, all_predictions)

print(f'Silhouette Score for Bathroom vs Price: {silhouette_avg_bathroom}')

silhouette_avg_bedroom = silhouette_score(X_Bedroom, bedroom_predictions)

print(f'Silhouette Score for Bedroom vs Price: {silhouette_avg_bedroom}')

