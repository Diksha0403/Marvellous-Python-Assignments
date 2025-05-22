def Factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact=fact*i
    
    print(no,"Factorial is: ",fact)
    
def main():

    num = int(input("Enter the Number: "))

    Factorial(num)   

if __name__ == "__main__":
    main()

