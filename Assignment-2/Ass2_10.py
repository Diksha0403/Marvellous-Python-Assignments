def AddNum():
    
    num = int(input("Enter the number: "))

    sum = 0
    for i in str(num):
        sum += int(i)
       
    print("The Addition of number is: ",sum)

    
AddNum()