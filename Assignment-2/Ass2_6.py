def Pattern2():
    print("Enter the no: ",end="")
    no = int(input())

    for i in range(no,0,-1):
        for j in range(0,i,1):
            print(" * ",end = " ")
        print()


Pattern2()