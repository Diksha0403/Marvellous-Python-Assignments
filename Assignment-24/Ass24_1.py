import pandas as pd
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler


def main():
    line = "*"*50
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Maths': [85, 90,78],
    'Science': [92,88, 80],
    'English': [75, 85,82]
    }

    Org_df = pd.DataFrame(data)

    print(line)
    print("Orignal Dataframe :\n")
    print(line)
    print(Org_df)


    Org_df['Normalized_Math_col'] = (Org_df['Maths'] - Org_df['Maths'].min()) / (Org_df['Maths'].max() - Org_df['Maths'].min())

    print(line)
    print("New Normalized Dataframe : \n")
    print(line)
    print(Org_df)


if __name__=="__main__":
    main()

