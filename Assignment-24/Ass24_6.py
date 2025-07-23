import pandas as pd

def Display():
    line = "*"*50
    Data = {'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]}
    
    df = pd.DataFrame(Data)
    print(line)
    print("Orignal Dataframe : \n ",df)
    print(line)

    df['Total']=df.sum(axis=1,numeric_only=True)

    df['Status'] = df['Total'].apply(lambda x : "Pass" if x>=250 else "Fail")

    print(line)
    print("Student Status : \n ",df)
    print(line)

    pass_df = df['Status'].value_counts()['Pass']

    print(line)
    print("Passed Sudent Count : ",pass_df)
    print(line)


def main():
    Display()

if __name__=="__main__":
    main()