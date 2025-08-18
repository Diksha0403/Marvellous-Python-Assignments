import pandas as pd
import numpy as np

def MissingValue():
     line = "*"*50
     data={'Marks':[85,np.nan,90,np.nan,95]}

     df = pd.DataFrame(data)

     print(line)
     print("Before Interpoletion : \n", df)
     print(line)

     interpolation_df = df.interpolate()

     print(line)
     print("Interpolated DataFrame: \n", interpolation_df)
     print(line)

def main():
    MissingValue()

if __name__=="__main__":
    main()