import pandas as pd
from sklearn.model_selection import train_test_split

def SplitData():
     line = "*"*50
     data={'Age':[25,20,45,35,22],'Salary':[50000,60000,80000,65000,45000],'Purchased':[1,0,1,0,1]}

     df=pd.DataFrame(data)

     print(line)
     print("Data before spliting")
     print(line)
     print(df)

     x = df[['Age','Salary']]
     y = df['Purchased']

     print(line)
     print("Data after spliting")
     print(line)

     x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

     print("Input train data set:\n", x_train)
     print(line)
     print("Output Train data set:\n", y_train)
     print(line)
     print("Test Data set:\n", x_test)
     print(line)
     print("Actual Output:\n", y_test)
     print(line)

def main():
    SplitData()

if __name__=="__main__":
    main()