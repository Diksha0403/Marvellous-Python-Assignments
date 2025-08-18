import pandas as pd
from sklearn import preprocessing

def lableoncity():
     border = "*"*50
     data={'City':['Pune','Mumbai','Delhi','Pune','Delhi']}

     org_df = pd.DataFrame(data)

     print(border)
     print("Before LableEcoding : \n" , org_df)
     print(border)

     leb_df = preprocessing.LabelEncoder()
     org_df['City'] = leb_df.fit_transform(org_df['City'])
     
     print(border)
     print("Data after Encoding : \n" ,org_df)
     print(border)


def main():
    lableoncity()

if __name__=="__main__":
    main()