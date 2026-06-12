# Housie Price Prediction&nbsp;&nbsp;
### Objective 
The objective of this project is to build a machine learning model that can accurately predict house prices based on various features such as area,number of bedrooms,bathrooms,number of stories,parking availability,and other property-related attributess.The project focuses on understanding th relationship between different housing features and the price of a property.Data preprocessing techniques are applied to handle missing values,remove duplicates,and convert categorical features(such as mainroad,guestroom,furnishing status,etc.) into numerical format using encoding methods.Overall,the goal is to develop a reliable model that can assist in estimating property prices based on key features,which can be buyers,sellers,and real estate analysis
### sample Dataset
<img width="771" height="262" alt="image" src="https://github.com/user-attachments/assets/90f2fc27-3e3c-4717-b014-803db4b45aa2" />

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

<img width="592" height="138" alt="image" src="https://github.com/user-attachments/assets/1225a1ee-6dff-49f4-835a-0f3515857c93" />
<img width="546" height="180" alt="image" src="https://github.com/user-attachments/assets/e2bec6bf-1a75-492a-89c2-3ea284ab439f" />
<img width="710" height="408" alt="image" src="https://github.com/user-attachments/assets/381b48bf-bfd9-42ef-a3de-6d367d389896" />

  + The Linear Regression model was successfully implemented to predict house prices based on various features.The model's performance was evaluted using Mean Squared Error (MSE) and R^2 score
  + The Mean Squared Error(MSE) obtained is 175,431,868,730,703,which indicates the average squared difference between the actual and predicted house prices. The relatively high value suggests that there is some deviation between predicted and the actual values,which is commom in datasets with large price ranges.
  + The R^2 score achieved is 0.6529,which means that approximately 65.29% of the variation in house prices is explained by the model.This indicates that the model has a moderate level of accuracy and is able to capture the relationship between features and target variable reasonably well.
  + The scatters plot of Actual vs Predicted House Price shows a positive trend,where most points follow a diagonal pattern.This indicates that the model predictions are fairly aligned with actual values,although some deviations are present.
  + Overall, the model performs reasonably well but can be furthur improved by using advanced models or additional feature engineering to enhance prediction accuracy.
    
