import os
import sys

def main():
    print("Enetr FIle Name: ")
    FileName = input()

    print("Enter the Search String: ")
    SearchStr = input()

    if os.path.exists(FileName):
        Fobj = open(FileName,"r")
        Data = Fobj.read()
        count = Data.count(SearchStr)
        print("The word frequency is: ",count)
        

if __name__ == "__main__":
    main()