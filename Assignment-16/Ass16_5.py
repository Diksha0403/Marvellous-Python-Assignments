import os

def readFileContent(fileName):
    try:
        Border="-"*55
        
        fileSize=os.path.getsize(fileName)
        print(f"File Name :'{fileName}'\nFile size:{fileSize} bytes")
        
        if(fileSize==0):
            print(f"File contains no data...\nFile is Empty.")
        else:  
            print(Border+"\n") 
                
            countWordsAndDisplayLine(fileName)  
            print(Border+"\n")             
    except Exception as errObj:
        print("\nError while reading file:",errObj)           


def countWordsAndDisplayLine(fileName):
    try:    
        dataCount=0
        print("Printing lines with word count > 5")
        
        fileObj=open(fileName,"r")
        
        fileLine=fileObj.readline()
        while fileLine:
            wordList=str(fileLine).split()
            if(len(wordList)>5):
                print(fileLine)
                dataCount=dataCount+1
            fileLine=fileObj.readline()
        if(dataCount==0):
            print("No lines found with given condition...Exiting program")
   
        fileObj.close()  
    except UnicodeDecodeError as errObj:
        print("\nInvalid File type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj) 


def main():
   
    fileName=input("Enter the file name:")
    readFileContent(fileName)
    


if __name__=="__main__":
    main()