import os

def main():
     print("Enter the file name: ")
     FileName = input()

     Fobj = open(FileName,"w")

     Fobj = open(FileName,"r")
     data = Fobj.read()
     
     print("\nData From File is:\n",data)

     Fobj.close()
if __name__ == "__main__":
    main()