import pandas as pd

def normalization():
    Line = "*"*50
    data={'Age':[18,22,25,30,35]}
    df = pd.DataFrame(data)

    print("Befor Normalization : \n",df)

    df['Age'] = (df['Age']-df['Age'].min())/(df['Age'].max()-df['Age'].min())

    print(Line)
    print("Normalised Data Frame")
    print(df)
    print(Line)


def main():
    normalization()

if __name__=="__main__":
    main()