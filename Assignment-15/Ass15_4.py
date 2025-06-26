import os
import sys

def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    if os.path.exists(FileName1) and os.path.exists(FileName2):
        F1= open(FileName1,"r")
        F2= open(FileName2,"r")

        data1=F1.read()
        data2=F2.read()

        if data1==data2:
            print("Success, File Content data is same")
        else:
            print("Comaprison Failed, file can't be same ")
            F1.close()
            F2.close()
    else:
        print("File doesn't exist")



if __name__=="__main__":
    main()