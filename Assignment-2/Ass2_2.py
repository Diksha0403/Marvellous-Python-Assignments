def Pattern1():
    print("Enter the no: ",end="")
    no = int(input())

    for i in range(0,no,1):
        for j in range(0,no,1):
            print(" * ",end = " ")
        print()


Pattern1()