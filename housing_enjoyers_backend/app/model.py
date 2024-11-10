import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from sklearn.preprocessing import StandardScaler
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


data_path = os.path.join(current_dir, "models", "Cleaned_Datasets", "Dataset_Combined.csv")

# Class for training and predicting with a Linear Regression model
class LinearRegressionModel:
    def __init__(self):

        # Initialize the Linear Regression model
        self.model = LinearRegression()

    # Function to fetch data for Line Chart
    def predict(self):
        data = pd.read_csv(data_path) #change path based on project directory

        X = data[['Rooms']]  # Features for the model

        y = data['Price'] 

        # Train the model
        self.model.fit(X, y)

        # Save the model to a file
        joblib.dump(self.model, 'linear.pkl')

        # Evaluate the model
        predictions = self.model.predict(X)
        mse = mean_squared_error(y, predictions)
        r2 = r2_score(y, predictions)
        print(f"Linear Regression Model trained. MSE: {mse}, R²: {r2}")
        print(predictions)

        # Format the response with time and prediction values for each row
        response = []
        for i, row in data.iterrows():
            date = row["Date"]
            predicted = predictions[i]
            response.append({'x': date, 'y': round(predicted, 2)})

        return response
    
    
    
    
# Class for training and predicting with a KMeans clustering model
class KMeansModel:
    def __init__(self):
        # Initialize the KMeans model with 3 clusters 
        self.model = KMeans(n_clusters=3)       

    def predict(self):


        data = pd.read_csv(data_path)#change path based on project directory

        # Select feature based on the specified target variable
        X = data[['Price', 'Bathroom']]


        # Train the model
        self.model.fit(X)

        # Save the model to a file
        joblib.dump(self.model, 'kmeans.pkl')

        # Assign clusters to the training data
        clusters = self.model.predict(X)
        data['Cluster'] = clusters # Add cluster labels to the dataset
        print("KMeans Model trained. Cluster assignments added to data.")


        # Map cluster numbers to descriptive levels and prepare response
        response = []
        for i, row in data.iterrows():
            cluster = int(clusters[i])
            if cluster == 0:
                response.append({"Level": "Low", "cluster": cluster})
            elif cluster == 1:
                response.append({"Level": "Moderate", "cluster": cluster})
            elif cluster == 2:
                response.append({"Level": "High", "cluster": cluster})

        print()
        return response
    







if __name__ == "__main__":    
    # Linear Regression Model
    linear_model = LinearRegressionModel()
    linear_model.predict()

    # KMeans Model
    kmeans_model = KMeansModel()
    kmeans_model.predict()
