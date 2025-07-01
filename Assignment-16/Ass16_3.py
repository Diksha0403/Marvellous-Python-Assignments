import os

Border="-"*57

def readFileContent(fileName):
    try:
        fileSize=os.path.getsize(fileName)
    
        print(f"File Name :'{fileName}'\nFile size is :{fileSize} bytes")
        if(fileSize==0):
            print(f"\nNothing to display from file ,Empty file")
        else:
            
            countNumberOfLinesWordChar(fileName)
             
    except UnicodeDecodeError as errObj:
        print("\nInvalid FIle type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj)          

def countNumberOfLinesWordChar(fileName):
    try:
        fileObj=open(fileName,"r")
        
        fileData=fileObj.readlines()

        print(Border+"\n") 
        print("Number of lines,words and character in the file")  
        print(Border+"\n") 

        
        lineCount=len(fileData)
        wordCount=0
        charCount=0

        for lineData in fileData:
            wordList=str(lineData).split()
            wordCount=wordCount+ len(wordList) 
            for charList in wordList: 
                charCount=charCount+len(charList)
                
        print(f"Number of Lines      : {lineCount}")
        print(f"\nNumber of Words      : {wordCount}")
        print(f"\nNumber of Characters : {charCount}")


        fileObj.close()  
    except UnicodeDecodeError as errObj:
        print("\nInvalid FIle type:",errObj)   
    except Exception as errObj:
        print("\nError while reading file:",errObj)      


def main():
    fileName=input("Enter the file name:")
    readFileContent(fileName)

if __name__=="__main__":
    main()