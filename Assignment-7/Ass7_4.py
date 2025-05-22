from functools import reduce

Product = lambda A,B: A*B

def main():
    data = list()

    size = int(input("Enter the Size: "))

    for i in range(size):
        no = int(input())
        data.append(no)

    RData = reduce(Product,data)
    print("Product: ",RData)


if __name__=="__main__":
    main()