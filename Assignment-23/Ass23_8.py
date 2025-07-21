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

    subject_col = ['Maths','Science','English']

    df['Total'] = df[subject_col].sum(axis=1)

    df['Total'] = df['Maths']+df['Science']+df['English']

    marks = df[df['Name']=='Amit'][['Maths','Science','English']]
    subject = ['Maths','Science','English']

    print(marks)

    plt.plot(subject,marks, marker = 'o')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit Report")
    plt.grid(True)
    plt.show()




if __name__=="__main__":
    main()