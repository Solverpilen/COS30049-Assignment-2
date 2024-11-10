import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

WorkingDirectory = "COS30049-Assignment-2/"
RawDataDirectory = WorkingDirectory + "Raw Datasets/"
CleanDataDirectory = WorkingDirectory + "Cleaned Datasets/"

Data = pd.read_csv(CleanDataDirectory + "Dataset_Combined.csv")
X = Data[["Date"]]
y = Data["Price"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the results on the test set
y_pred = model.predict(X_test)

# Print model performance
print('Mean Squared Error: %.2f' % mean_squared_error(y_test, y_pred))
print('R^2 Score: %.2f' % r2_score(y_test, y_pred))

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black', label='Actual values')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted values')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Linear Regression on Melbourne Housing Dataset')
plt.legend()
plt.show()