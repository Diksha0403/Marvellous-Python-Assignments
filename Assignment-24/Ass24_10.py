import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    line = "*"*50
    Data = {'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]}
    
    df = pd.DataFrame(Data)
    print(line)
    print("Orignal Dataframe : \n ",df)
    print(line)

    sns.boxplot(x='Name',y='English',data=df)
    plt.title("Box Plot of English Data")
    plt.show()

if __name__=="__main__":
    main()