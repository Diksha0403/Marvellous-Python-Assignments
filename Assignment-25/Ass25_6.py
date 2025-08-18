import pandas as pd

def lableEncoding():
    BORDER = "*"*50
    data={'Grade':['A+','B','A','C','B+']}
    gradeMappingDict={'A+':'Excellent','A':'Very Good','B+':'Good',"B":"Average",'C':'Poor'}
    grade_df = pd.DataFrame(data)

    print(BORDER)
    print("\nDataFrame Before replacement:")
    print(grade_df)
    print(BORDER)

    grade_df.replace({"Grade": gradeMappingDict},inplace=True)
    print("\nDataFrame after replacement:")
    print(grade_df)
    print(BORDER)

def main():
    lableEncoding()

if __name__=="__main__":
    main()