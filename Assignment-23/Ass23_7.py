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

    df['Total'] = df['Maths']+df['Science']+df['English']

    print(df)
    
    fig = plt.figure(figsize= (8,6))
    plt.bar(df['Name'],df['Total'])
    plt.title("Marvellous Barplot for Student Name by Total Marks")
    plt.xlabel('Student Name')
    plt.ylabel('Total Marks')
    plt.show()    



if __name__=="__main__":
    main()