import os

def main():
    print("Enter File Name: ")
    FileName = input()

    F1 = open(FileName,"w")

    for i in range(5):
        StudName = input("Enter Student Name: ")
        F1.write(StudName+"\n")
        i = i+1
    F1.close()

if __name__ == "__main__":
    main()