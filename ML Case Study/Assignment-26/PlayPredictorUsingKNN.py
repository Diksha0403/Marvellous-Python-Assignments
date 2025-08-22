import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

BORDER="-"*65
FILENAME="PlayPredictor.csv"

def loadDataSet():
    df_PlayPredictor = pd.read_csv(FILENAME)

    print(BORDER)
    print("PlayPredictor Data set load successfully...")
    print(BORDER)
    print(df_PlayPredictor.head())
    print(df_PlayPredictor.shape)
    print(BORDER)
    return df_PlayPredictor

def cleanDataSet(df_PlayPredictor):
   
    df_cleanDataset = df_PlayPredictor.drop(columns=['Unnamed: 0'],inplace=True)
    
    df_PlayPredictor.dropna(inplace=True)

    print("Play data set after removing column...")
    print(BORDER)
    print(df_PlayPredictor.head())


def prepareDataset(df_cleanDataset):
    for col in df_cleanDataset.select_dtypes(include='object'):
        df_cleanDataset[col]=preprocessing.LabelEncoder().fit_transform(df_cleanDataset[col])

    print(BORDER)
    print("Encoded Data frame")
    print(BORDER)
    print(df_cleanDataset.head())
    return df_cleanDataset

def splitData(df_cleanDataset):
    x = df_cleanDataset[['Whether','Temperature']]  
    y = df_cleanDataset['Play']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    return x_train,x_test,y_train,y_test
    
def trainDataSet(x_train,y_train):
    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)
    return model

def testDataSet(model,x_test):
    y_pred = model.predict(x_test)
    print("Testing Result : ", y_pred)
    return y_pred

def CheckAccuracy(y_test,y_pred):
    Accuracy = accuracy_score(y_test,y_pred)
    return Accuracy

def main():
    """Step-1 : Get the Play predictor data set"""
    df_play = loadDataSet()

    """Step-2 : """
    cleanDataSet(df_play)

    prepareDataset(df_play)

    """Step-3 : Train data"""
    x_train, x_test, y_train, y_test = splitData(df_play)
    model = trainDataSet(x_train,y_train)
    print("Model build successfully......")

    """step-4 : test Data set"""
    print("test Data set")
    y_pred = testDataSet(model,x_test)
    

    """step-5: Check Accuracy"""
    accu_ret = CheckAccuracy(y_test,y_pred)
    print("Accuracy is : ",accu_ret*100)
    
if __name__=="__main__":
    main()

