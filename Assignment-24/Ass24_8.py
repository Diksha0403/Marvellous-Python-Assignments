import pandas as pd
import matplotlib.pyplot as plt

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

    # plt.figure(figsize= (8,6))
    plt.hist(df['Math'],bins=10,color="green",edgecolor="black")
    plt.title("Histogram - Math Marks")
    plt.xlabel("Marks")
    plt.ylabel("Range")
    plt.show()

if __name__=="__main__":
    main()