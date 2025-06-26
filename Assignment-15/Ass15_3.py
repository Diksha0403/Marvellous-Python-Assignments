import os
import sys

def main():
    print("ENter into the ABC file")
    source_file = sys.argv[1]

    print("Enter New file name: ")
    FileName = input()

    fobj = open(source_file,"r")
    data = fobj.read()

    fobj1 = open(FileName,"w")
    fobj1.write(data)

    print("Data is sucessfully copied into the Demo file")

    fobj.close()
    fobj1.close()



if __name__ == "__main__":
    main()