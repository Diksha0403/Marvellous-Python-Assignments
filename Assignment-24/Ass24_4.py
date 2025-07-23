import pandas as pd
import matplotlib.pyplot as plt

def Display():
    line = "*"*50
    Data = {'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]}
    
    df = pd.DataFrame(Data)

    print(line)
    print("Origanl Dataframe : \n ",df)
    print(line)

    name_df = df[df['Name'] == 'Sagar'].iloc[0]
    marks = [name_df['Math'],name_df['Science'],name_df['English']]
    subject = ['Math','Science','English']

    plt.figure(figsize= (8,6))
    plt.pie(marks,labels=subject,autopct='%1.1f%%')
    plt.title('Sagar Report')
    plt.show()

def main():
    Display()


if __name__ == "__main__":
    main()