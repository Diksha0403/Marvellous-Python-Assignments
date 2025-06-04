from functools import reduce

CheckNum = lambda no: (no % 2 == 0)
Increase =lambda no:no**2
Product = lambda A,B : A + B

def main():
    data =[]
    size = int(input("enter number of element:"))
    print("Please enter the values in list")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("Input Data: ",data)

    FData = list(filter(CheckNum,data))
    print("Filtered Output: ",FData)

    MData = list(map(Increase,FData))
    print("Mapping Output: ",MData)

    RData = reduce(Product,MData)
    print("reduce Output",RData)


if __name__ == "__main__":
    main()