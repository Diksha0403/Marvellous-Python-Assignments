#Recursion
sum= 0
def sum_of_digit(no):
    global sum

    if no >= 1:
        sum = sum + no
        no = no - 1
        sum_of_digit(no)
    return sum

def main():
    ret = sum_of_digit(4)
    print("sum_of_digit using Recursion", ret)

if __name__ == "__main__":
    main()


#Iteration

def sum_of_digit(no):
    sum= 0
    for i in range(1,no+1):
        sum = sum + i
        no = no - 1
    return sum

def main():
    ret = sum_of_digit(4)
    print("sum_of_digit using Iteration: ",ret)

if __name__ == "__main__":
    main()
