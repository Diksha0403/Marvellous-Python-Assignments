PrimeNo = lambda no : (no>1) and all(no%i != 0 for i in range(2,no))

def main():
    data = list()

    n = int(input("Enter the number: "))

    for i in range(n):
        no = int(input())
        data.append(no)

    print("Input List: ",data)

    Fdata = list(filter(PrimeNo,data))
    print("Prime Number: ",Fdata)

if __name__ == "__main__":
    main()