import pandas as pd
import numpy as np


def main():
    line = "*"*50
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Maths': [np.nan, 76,88],
    'Science': [91,np.nan, 85]
    }

    df = pd.DataFrame(data)

    print(line)
    print("Student marks Original Dataframe with missing values :\n")
    print(line)

    print(df)

    df.fillna(df.mean(numeric_only=True),inplace=True)

    print(line)
    print("\n DataFrame after filling missing values with column mean:")
    print(line)

    print(df)


if __name__=="__main__":
    main()