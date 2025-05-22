def PrimeNum(no):

    if no<=1:
        print("Not a prime number")
        return
    
    for i in range(2,no):
        if(no % i == 0):
            print("Not a prime Number")
            return
    
    print("It's Prime Number")

def main():
    num = int(input("Enter the Number: "))

    PrimeNum(num)

if __name__ == "__main__":
    main()