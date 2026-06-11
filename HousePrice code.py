
#import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
#Load Dataset
df = pd.read_csv('Housing.csv')
df

#Identify missing values
df.isnull().sum()

#check duplicates
print("Duplicate Rows:",df.duplicated().sum())

#Dataset information
df.info()

#Features & Target
X= df.drop('price', axis=1)
y = df['price']

import pandas as pd
df = pd.read_csv("Housing.csv")
df_encoded = pd.get_dummies(df,drop_first=True,dtype=int)

print(df_encoded.head())

#Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
    )

X_processed = df_encoded.drop('price', axis=1)
y_processed = df_encoded['price']
X_train_processed, X_test_processed, y_train_processed, y_test_processed = train_test_split(X_processed, y_processed, test_size=0.2, random_state=42)

#Linear Regression
model= LinearRegression()
model.fit(X_train_processed, y_train_processed)

#Predictions
prediction = model.predict(X_test_processed)

# calculate MSE
mse =mean_squared_error(y_test, prediction)

print("Mean Squared Error:", mse)

#Caluculate R2score
r2=r2_score(y_test, prediction)
print("R-squared:", r2)

#Visualization between actual and predicted House Price
import matplotlib.pyplot as plt
plt.scatter(y_test, prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs. Predicted Prices")
plt.show()
