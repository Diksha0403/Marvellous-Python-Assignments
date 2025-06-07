#Recursion
sum= 0
def sum_of_n(no):
    global sum

    if no >= 1:
        sum = sum + no
        no = no - 1
        sum_of_n(no)
    return sum

def main():
    num = int(input("Enter the number: "))
    ret = sum_of_n(num)
    print("sum of first Natural number using Recursion", ret)

if __name__ == "__main__":
    main()


#Iteration

def sum_of_n(no):
    sum= 0
    for i in range(1,no+1):
        sum = sum + i
        no = no - 1
    return sum

def main():
    num = int(input("Enter the number: "))
    ret = sum_of_n(num)
    print("sum of first Natural number using Iteration: ",ret)

if __name__ == "__main__":
    main()
