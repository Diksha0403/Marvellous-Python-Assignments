import os
Border="-"*57

def readAndCleanFile(fileName):
    try:
        fileNamePrefix=fileName.split(".")
        updatedFileName=f"{fileNamePrefix[0]}_CLEAN.{fileNamePrefix[1]}"
        
        fileObj=open(fileName,"r")

        fileCleanDataObj=open(updatedFileName,"w")

        fileLineData=fileObj.readline()

        while(fileLineData):
            if(len(fileLineData)>1 and not(fileLineData.isspace())):
                fileCleanDataObj.write(str(fileLineData))

            fileLineData=fileObj.readline()

        fileObj.close()
        fileCleanDataObj.close()  

        print(f"\nCleaned data copied to file :'{updatedFileName}'") 
        
        print(Border)

    except FileExistsError as fileErr:
        print("File Not exists:",fileErr) 

    except FileNotFoundError as fileErr:
        print("File Not Found:",fileErr) 
        
    except Exception as excObj:
        print("Exception occured in readAndCleanFile() :",excObj)         
   


def main():
        print("\nThis is script for removing all blank lines from file")
        fileName=input("Enter file name :")
        readAndCleanFile(fileName)
    
if __name__=="__main__":
    main()