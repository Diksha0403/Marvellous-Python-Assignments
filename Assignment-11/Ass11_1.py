#Iteration
def number(no):
    print("Iteration")
    for i in range(1,no+1):
        print(i, end=" ")
    print()


def main():
    num = int(input("Enter The number: "))
    number(num)

if __name__ == "__main__":
    main()


#Recursion

def number(no):
    if no > 0:
        number(no-1)
        print(no, end=" ")


def main():
    num = int(input("Enter The number: "))
    print("Recursion")
    number(num)

if __name__ == "__main__":
    main()