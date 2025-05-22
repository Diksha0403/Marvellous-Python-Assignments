def main():

    sum = 0
    for no in range(1,101):
        if(no % 2 == 0):
            sum += no
            
    print("Sum of Even Num from 1 to 100 is: ",sum,end=" ")

if __name__ == "__main__":
    main()