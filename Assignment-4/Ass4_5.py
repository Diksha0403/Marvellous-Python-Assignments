from functools import reduce

Multi =lambda no:no*2
MaxNum = lambda no1,no2:max(no1,no2)

def PrimeNum(no):
    checkprime = True
    for i in range(2,no):
        if no % i == 0:
            checkprime = False
            break
    if checkprime == True:
        return no
    
# def Multi(no):
#     return no*2

# def MaxNum(no1,no2):
#     return max(no1,no2)


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