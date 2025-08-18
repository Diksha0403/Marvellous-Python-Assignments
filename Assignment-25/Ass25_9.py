import pandas as pd
import numpy as np

def ReplaceMarks():
    line = "*"*50
    data={'Marks':[45,67,88,32,76]}
    df = pd.DataFrame(data)

    print(line)
    print(df)
    print(line)

    df['Marks'] = df['Marks'].where(df['Marks']>=50,'Fail')

    print(line)
    print(df)
    print(line)

def main():
    ReplaceMarks()

if __name__=="__main__":
    main()