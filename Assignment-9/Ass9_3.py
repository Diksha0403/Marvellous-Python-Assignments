import multiprocessing.pool

def Factorial(no):
    fact = 1
    for i in range(2,no+1):
        fact *= i
    return fact

def main():
    data = [1,2,3,4,5]
    result = []

    p = multiprocessing.Pool()
    result = p.map(Factorial,data)

    p.close()
    p.join()
    
    print(result)
    
if __name__ == "__main__":
    main()