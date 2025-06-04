from functools import reduce

CheckNum = lambda no: (no >= 70 and no <= 90)
Increase =lambda no:no+10
Product = lambda x,y:x*y


def main():
    try:
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

    except ValueError:
        print("Please enter valid element into the list")



if __name__ == "__main__":
    main()