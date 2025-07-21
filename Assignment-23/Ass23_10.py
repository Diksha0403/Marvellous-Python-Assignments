import pandas as pd
import matplotlib.pyplot as plt

def main():
    line = "*"*50
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Maths': [85, 90,78],
    'Science': [92,88, 80],
    'English': [75, 85,82]
    }

    df = pd.DataFrame(data)

    print(line)
    print("Student marks Dataframe :\n")
    print(line)

    print(df)

    print(line)
    print("Drop the English column from Dataset")
    print(line)

    df.drop(columns = ['English'], inplace = True)

    print(line)
    print("Updated Dataset is : \n")
    print(line)

    print(df)


if __name__=="__main__":
    main()