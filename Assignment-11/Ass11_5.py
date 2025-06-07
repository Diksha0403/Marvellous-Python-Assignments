#Recursion

def count_zeros_recursive(num):
    if num == 0:
        return 1
    if num < 10:
        return 0
    if num % 10 == 0:
        return 1 + count_zeros_recursive(num // 10)
    else:
        return count_zeros_recursive(num // 10)
    
def main():
    num = int(input("Enter a number: "))
    ret = count_zeros_recursive(num)
    print("Zero count using recursive:", ret)


if __name__ == "__main__":
    main()



#Iteration

def count_zeros_iterative(num):
    count = 0
    if num == 0:
        return 1
    while num > 0:
        if num % 10 == 0:
            count += 1
        num //= 10
    return count

def main():
    num = int(input("Enter a number: "))
    ret = count_zeros_iterative(num)
    print("Zero count using iteration:", ret)

if __name__ == "__main__":
    main()
