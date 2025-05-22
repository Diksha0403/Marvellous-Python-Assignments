def Addition(val1,val2):
    ret = val1 + val2
    return ret

def Diffrence(val1,val2):
    ret = val1 - val2
    return ret

def Product(val1,val2):
    ret = val1 * val2
    return ret

def Division(val1,val2):
    ret = val1 / val2
    return ret


def main():
    no1 = int(input("Enter first Number: "))
    no2 = int(input("Enter Second Number: "))

    sum = Addition(no1,no2)
    print("Sum : ", sum)

    diffrence = Diffrence(no1,no2)
    print("Diffrence : ", diffrence)

    product = Product(no1,no2)
    print("Product : ", product)

    division = Division(no1,no2)
    print("Division : ", division)

    

if __name__ == "__main__":
    main()