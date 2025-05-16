def SumofFactor():

    num = int(input("Enter the number: "))
    sum_fact = 0

    for i in range(1,num):
        if num % i == 0:
            sum_fact += i
            print(i)
        
    print("The addition of factors is: ", sum_fact)

SumofFactor()
