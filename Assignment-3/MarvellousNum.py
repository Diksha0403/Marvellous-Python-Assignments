def ChkPrime(no):

    checkprime = True
    for i in range(2,no):
        if no % i == 0:
            checkprime = False
            break
    if checkprime == True:
        return no
    

