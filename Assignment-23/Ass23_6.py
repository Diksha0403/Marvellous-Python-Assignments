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
    print("Student marks Dataframe :\n")
    print(line)

    df['Total'] = df['Maths']+df['Science']+df['English']

    print(df)

    print(line)
    print("New Dataset with Total column in Desecnding Order: \n ")
    print(line)
    
    oredered_df = df.sort_values(by=['Total'], ascending=False)

    print(oredered_df)
    


if __name__=="__main__":
    main()