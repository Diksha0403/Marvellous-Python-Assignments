import pandas as pd

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
    print("Student marks Dataframe :\n","\n",df)
    print(line)

    print("\n Descriptive statistics of Data : \n",df.describe())


if __name__=="__main__":
    main()