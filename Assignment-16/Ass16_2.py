
import os

Border="-"*57

def readFileContent(fileName):
    try:       
        fileSize=os.path.getsize(fileName)

        print(f"File Name :'{fileName}'\nFile size:{fileSize} bytes")

        if(fileSize==0):
            print(f"File contains no data...\nFile is Empty.")
        else:
            fileObj=open(fileName,"r")
            fileData=fileObj.read()

            print(f"\nDisplaying '{fileName}' contents.......")   
            print(Border+"\n") 

            print(fileData)   
            fileObj.close()    

    except UnicodeDecodeError as errObj:
        print("\nInvalid File type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj)          
    print(Border+"\n")           

def main():
    try:
        fileName=input("Enter the file name:")
        readFileContent(fileName)
    except Exception as errObj:
        print("\nException in main():",errObj) 

if __name__=="__main__":
    main()

