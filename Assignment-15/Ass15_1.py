import os

def main():
    print("Enter the file name: ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret==True):
        print("File is exists")
    else:
        print("File is not exists")

if __name__ == "__main__":
    main()