# Housie Price Prediction&nbsp;&nbsp;
### Objective 
The objective of this project is to build a machine learning model that can accurately predict house prices based on various features such as area,number of bedrooms,bathrooms,number of stories,parking availability,and other property-related attributess.The project focuses on understanding th relationship between different housing features and the price of a property.Data preprocessing techniques are applied to handle missing values,remove duplicates,and convert categorical features(such as mainroad,guestroom,furnishing status,etc.) into numerical format using encoding methods.Overall,the goal is to develop a reliable model that can assist in estimating property prices based on key features,which can be buyers,sellers,and real estate analysis
### sample Dataset
<img width="1113" height="366" alt="image" src="https://github.com/user-attachments/assets/d0e7e5b3-21af-40f5-a5b7-c90f7d6df35a" />


### Dataset Overview
+ The dataset contains information about different houses and their features.
+ Each row represents a single house, and each column represents a specific feature of that house.
+ The purpose of this dataset is to predict house price using machine learning ,Analyze how different features affect price and assist in real estate decision making
+ The main goal of the dataset is to predict house prices based on various attributes

### Tools and Technologies
+ Google Cloab - Cloud-based environment for writing and executing Python code
+ Python - Core programming language used for implementation
+ Pandas-Used for data manipulation,cleaning,and preprocessing.
+ NumPy- Used for  numerical operations and handling arrays.
+ Matplotlib - Used for visualization
+ Data Encoding (pg.get_dummies)- Converts categorical data into numerical form
+ LinearRegression - Used to bulid the prediction model
+ mean_squared_error(MSE)-Used to measure prediction error
+ r2_score-Used to measure model performance (accuracy of regression)

   ### Steps in Housing Price Prediction
  1.Import Libraries
     + Pandas -> data handling
     + NumPy -> numerical computations
     + Seaborn & Matplotlib-> visualization
  
  2.Load Dataset
     + Loaded the dataset using 'pandas.read_csv()'
  
  3.Data Exploration
     + Checked missing values using 'df.isnill().sum()'
     + Checked duplicate rows and removed them if present
     + Viewed dataset information using'df.info()'

   4.Data Preprocessing
     + Identified categorical columns (yes/no,furnishing status)
     + Converted categorical data into  umerical format using 'pd.get_dummies()'

   5.Feature selection
     + X(Features) - all columns except 'price'
     + y(Target)- 'price' column

   6.Train-Test Split
     + Split data into training(80%)and testing(20%)

   7.Model Training
     + USed Linear Regression model to train model using training data
  
  8.Prediction
     + Predicted house price using the test data

   9.Model Evaluation
     + Mean Square Error (MSE) - measure prediction error
     + R^2 Score - measures model performance

   10.Visualization
     + Plotted graph between actual prices (y_test)and prices (predictions)
     + Used scatter plot for comparison

   ### Outcome

<img width="786" height="156" alt="image" src="https://github.com/user-attachments/assets/aea14f67-1a3b-42e4-9f2c-94e096f26e08" />
<img width="472" height="107" alt="image" src="https://github.com/user-attachments/assets/7b61d15e-79b3-4a4d-a4e8-f3d06d12d99c" />
<img width="816" height="576" alt="image" src="https://github.com/user-attachments/assets/cc0e46e4-19d0-4134-87ae-186d137fbaac" />


  + The Linear Regression model was successfully implemented to predict house prices based on various features.The model's performance was evaluted using Mean Squared Error (MSE) and R^2 score
  + The Mean Squared Error(MSE) obtained is 1754318687330.6638,which indicates the average squared difference between the actual and predicted house prices. The relatively high value suggests that there is some deviation between predicted and the actual values,which is commom in datasets with large price ranges.
  + The R^2 score achieved is 0.6529,which means that approximately 65.29% of the variation in house prices is explained by the model.This indicates that the model has a moderate level of accuracy and is able to capture the relationship between features and target variable reasonably well.
  + The scatters plot of Actual vs Predicted House Price shows a positive trend,where most points follow a diagonal pattern.This indicates that the model predictions are fairly aligned with actual values,although some deviations are present.
  + Overall, the model performs reasonably well but can be furthur improved by using advanced models or additional feature engineering to enhance prediction accuracy.
    
