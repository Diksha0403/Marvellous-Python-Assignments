from MarvellousNum import ChkPrime

def ListPrime():
    size = int(input("Enetr the number of element "))

    data = list()

    print("Enter the element:")
    for i in range(size):
        no = int(input())
        data.append(no)

    PrimeNum = list()
    for no in data:
        if ChkPrime(no):
            PrimeNum.append(no)

    # print("Prime Numbers:", PrimeNum)
    print("Output:", sum(PrimeNum), PrimeNum)


ListPrime()
