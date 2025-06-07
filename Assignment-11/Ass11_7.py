#Recursion
def pattern(no):
    
    if no > 1:
        pattern(no-1)
    print(" * "*no,end=" ")
    print()    


def main():
    num = int(input("Enter the number: "))
    print("Recursion")
    pattern(num)
    
if __name__ == "__main__":
    main()


#Iteration

def pattern(no):
    for i in range(0,no+1):
        for j in range(0,i,1):
            print(" *",end = " ")
        print()

def main():
    num = int(input("Enter the number: "))
    print("Iteration")
    pattern(num)
    

if __name__ == "__main__":
    main()
