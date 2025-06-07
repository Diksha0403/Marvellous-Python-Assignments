#Recursion

fact = 1

def factorial(no):
    global fact
    if no > 1:
        fact = fact * no
        no = no - 1
        factorial(no)
    return fact

def main():
    num = int(input("Enter the Number: "))
    ret = factorial(num)
    print("Recursion: ", ret)
    

if __name__ == "__main__":
    main()



#Iteration
def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    return fact

def main():
    num = int(input("Enter the number: "))
    ret = factorial(num)
    print("Iteration: ",ret)

if __name__ == "__main__":
    main()