def NumPattern():
    print("Enter the no: ",end="")
    no = int(input())

    for i in range(0,no,1):
        for j in range(1,no+1):
            print(j ,end = " ")
        print()


NumPattern()