import pandas as pd
from sklearn.preprocessing import OneHotEncoder 


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

    df['Gender']=df['Gender'].map({'Male':1,'Female':2})   

    print(line)
    print("One-hot encoded Dataframe : \n",df)
    print(line)
  
   
def main():
     Display()



if __name__ =="__main__":
    main()    
