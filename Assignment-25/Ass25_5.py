import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    border = "*"*50
    data={'Age':[22,25,47,52,46,56],'Purchased':[0,1,1,0,1,0]}

    df = pd.DataFrame(data)

    print(border)
    print("Data before spliting")
    print(border)
    print(df)

    print(border)
    print("Data After Spliting")
    print(border)

    x = df['Age']
    y = df['Purchased']
    
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    print("Input train data set:\n")
    print(x_train)
    print(border)
    print("Output Train data set:\n")
    print(y_train)
    print(border)
    print("Test Data set:\n")
    print(x_test)
    print(border)
    print("Actual Output:\n")
    print(y_test)
    print(border)

if __name__=="__main__":
    main()