import pandas as pd

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
    
    gender_list = ['Male','Male','Female']
    df['Gender'] = gender_list

    print(line)
    print("Gender Column added : \n ",df)
    print(line)

    avg_mark = df.groupby('Gender')[['Math','Science','English']].mean()

    print(line)
    print("Avrange marks : \n ", avg_mark)
    print(line)
  
   
def main():
     Display()



if __name__ =="__main__":
    main()    
