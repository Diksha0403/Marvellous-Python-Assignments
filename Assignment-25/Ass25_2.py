import pandas as pd
import numpy as np

def findcolDatatype():
    border = "*"*50
    data={'Name':['A','B','C'],'Age':[21.0,22.0,23.0]}
    df = pd.DataFrame(data)

    print(border)
    print("Column DataType is:  ")
    print(border)
    print(df.dtypes)

    df = df.astype({'Age':int})

    print(border)
    print(df)
    print(border)


def main():
    findcolDatatype()

if __name__=="__main__":
    main()
