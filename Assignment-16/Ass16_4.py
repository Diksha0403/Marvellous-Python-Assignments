import os

def main():
        
        fobj=open("Number.txt","w")

        print("Enter numbers:")

        for i in range (10):
            no=int(input())
            fobj.write(str(no)+"\n")
            i=i+1

        fobj.close()
   
if __name__=="__main__":
    main() 
