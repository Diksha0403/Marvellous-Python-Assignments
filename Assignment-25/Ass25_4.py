import pandas as pd

def OnehotEncoding():
    border = "*"*50
    data={'Department':['HR','IT','Finance','HR','IT']}
    
    df = pd.DataFrame(data)

    print(border)
    print("befor one-hot Encoding : \n")
    print(df)
    print(border)

    df_encoding = pd.get_dummies(df,columns=['Department'])

    print(border)
    print("After one-hot Encoding : \n")
    print(df_encoding)
    print(border)


def main():
    OnehotEncoding()

if __name__=="__main__":
    main()

