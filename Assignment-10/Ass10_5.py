from functools import reduce

PrimeNum = lambda no: (no>1) and all(no%i != 0 for i in range(2,no))
Multi =lambda no:no*2
MaxNum = lambda no1,no2:max(no1,no2)


def main():
    data =[]
    size = int(input("enter number of element:"))
    print("Please enter the values in list")
    for i in range(size):
        no=int(input())
        data.append(no)

    print("Input Data: ",data)

    FData = list(filter(PrimeNum,data))
    print("Filtered Output: ",FData)

    MData = list(map(Multi,FData))
    print("Mapping Output: ",MData)

    RData = reduce(MaxNum,MData)
    print("reduce Output",RData)


if __name__ == "__main__":
    main()