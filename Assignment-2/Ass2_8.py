
def NumPattern1():
    print("Enter the no: ",end="")
    no = int(input())

    for i in range(0,no+1,1):
        for j in range(1,i+1,1):
            print(j, end=" ")
        print()

NumPattern1()
