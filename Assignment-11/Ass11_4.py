#Recursion
ret = 1
def power(x, n):
    global ret
    if n!=0:
        ret = ret * 2
        power(x, n-1)
    return ret

def main():
    x = int(input("Enter base: "))
    n = int(input("Enter exponent: "))
    ret = power(x, n)
    print("Recursion Result:", ret)

if __name__ =="__main__":
    main()



# Iteration
def power(x, n):
    ret = 1
    for i in range(n):
        ret = ret * 2
    return ret

def main():
    x = int(input("Enter base: "))
    n = int(input("Enter exponent: "))
    ret = power(x, n)
    print("Iteration Result:", ret)

if __name__ =="__main__":
    main()