"""---------------------------------------------------------------------------------------------------------
Problem statement:Dataset contains information about Advertisement agenecy
--------------------------------------------------------------------------------------------------------"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt


Border = "*"*50

"""---------------------------------------------------------------------------------
#  This method loads the data set from 'Advertising.csv' file
#  Input params : Data file path
#  Output : Data frame
#---------------------------------------------------------------------------------"""

def loadDataSet():
    load_df = pd.read_csv("Advertising.csv")

    print(Border)
    print("Adverstise Sales data loaded successfully...")
    print(Border)
    print(load_df.head())
    print(load_df.shape)
    print(Border)
    return load_df

"""---------------------------------------------------------------------------------
#  This method cleans data frame
#  input Params :  load_df(sales data frame)
#  Removes unwanted data and coulmns from data frame
#---------------------------------------------------------------------------------"""

def cleanDataSet(load_df):
    load_df.drop(columns=['Unnamed: 0'],inplace=True)
    load_df.dropna(inplace=True)
    print(Border)
    print("Data set after cleaning....")
    print(Border)
    print(load_df)
    print(Border)

"""---------------------------------------------------------------------------------------------------------
# Extracting Features/Independent and Label/Dependent variables
# Input params: load_df(Sales data Frame)
# Output : x-Independent,y-Dependent variables
#-------------------------------------------------------------------------------------------------------"""


def FeatureLable(load_df):
    x = load_df[['TV','radio','newspaper']]
    y = load_df['sales']
    return x ,y

"""---------------------------------------------------------------------------------------------------------
#  Train data set using linear regression algorithm
#  Input params : x-Independent(Features : TV,Radio,NewsPapaer)
#                 y-Dependent(Label : sales)  
#  Output : Return model built                
#---------------------------------------------------------------------------------------------------------"""


def TrainTestDataSet(x,y):
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    model = LinearRegression()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)

    meanSquaredError = metrics.mean_absolute_error(y_test,y_pred)
    rootmeanSquarederror = np.sqrt(meanSquaredError)
    r2 = metrics.r2_score(y_test,y_pred)

    print(Border)
    print("Mean Square error : ", meanSquaredError)
    print("Root mean Square Error : ", rootmeanSquarederror)
    print("R square value : ", r2)  

    print("Model Coefficient are : ")
    for col,coef in zip(x.columns,model.coef_):
        print(f"{col}:{coef}")

    print("Y Intercept is : ",model.intercept_)
    return y_test,y_pred

"""---------------------------------------------------------------------------------------------------------
#   Display Actual Result vs Predicted Result
#---------------------------------------------------------------------------------------------------------"""
def displayPredictedVsActualSales(y_test,y_pred):
    print(Border)
    dfTest=pd.DataFrame({"Actual Sale":y_test,"Predicted Sales":y_pred})
    print(Border)
    print(dfTest)
    print(Border)

"""---------------------------------------------------------------------------------------------------------
#   Plot Actual Result vs Predicted Result
#---------------------------------------------------------------------------------------------------------"""

def PlotGraph(y_test,y_pred):
    plt.figure(figsize=(8,5))
    plt.scatter(y_test,y_pred,color = 'blue')
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Advertiesment")
    plt.grid(True)
    plt.show()

#---------------------------------------------------------------------------------------------------------
#  Main function 
#---------------------------------------------------------------------------------------------------------
def main():
   load_data =  loadDataSet()

   cleanDataSet(load_data)

   x,y = FeatureLable(load_data)

   y_test,y_pred = TrainTestDataSet(x,y)

   displayPredictedVsActualSales(y_test,y_pred)

   PlotGraph(y_test,y_pred)

#---------------------------------------------------------------------------------------------------------
#Main entry point of the program
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
