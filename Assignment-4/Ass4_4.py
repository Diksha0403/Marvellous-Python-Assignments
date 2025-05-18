from functools import reduce

CheckNum = lambda no: (no % 2 == 0)
Increase =lambda no:no**2
Product = lambda A,B : A + B

# def filter(Task,Values):
#     Result = []
#     for no in  Values:
#         ret = (Task(no))
#         if (ret == True):
#             Result.append(no)
#     return Result

# def map(Task,Values):
#     Result = []
#     for no in Values:
#         ret = (Task(no))
#         Result.append(ret)

#     return Result


# def reduce(Task,Values):
#     Result = 0
#     for no in Values:
#         Result = (Task(Result,no))
#     return Result

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