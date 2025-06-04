Multiplication = lambda A,B : A*B

def main():
    try:
        num1= int(input("Enter first num: "))
        num2= int(input("Enter second num: "))

        Ret = Multiplication(num1,num2)
        
        print("Multiplication is: ",Ret)

    except ValueError:
        print("Please enter valid integers.")

if __name__=="__main__":
    main()