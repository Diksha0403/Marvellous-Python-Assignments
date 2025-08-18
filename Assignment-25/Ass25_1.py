import pandas as pd
import numpy as np

def DetectOutliear():
     BORDER = "*"*50
     data={'Salary':[25000,27000,29000,31000,50000,100000]}

     df = pd.DataFrame(data)

     print(df)

     Q1=df['Salary'].quantile(0.25)
     Q3=df['Salary'].quantile(0.75)

     IQRsal = Q3-Q1
     print("IQR Value: ",IQRsal) # Interquartile Range (IQR)

     

     below = Q1 - 1.5*IQRsal
     above = Q3 + 1.5*IQRsal     

     Outliers = df[(df['Salary']<below) | (df["Salary"]>above)]
    

     print("Lower bound is:",below)
     print("Upper Bound is :",above)
     print(BORDER)
     print("\nOutliers are: \n", Outliers)
     print(BORDER)

def main():
    DetectOutliear()

if __name__=="__main__":
    main()