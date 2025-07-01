def copyFile(srcFile,destFile):
    try:
        srcObj=open(srcFile,"r")
        destObj=open(destFile,"w")

        srcData=srcObj.read()
        destObj.write(srcData)

        print(f"\nSuccessfuly copied data from '{srcFile} to '{destFile}'")

        srcObj.close()
        destObj.close()         
    except Exception as exc:
        print("Exception in file:",exc)            

def main():
    sourceFile=input("\nEnter Source file name:")
    destinationFile=input("\nEnter Target file name:")
   
    copyFile(sourceFile,destinationFile)

if __name__=="__main__":
    main()