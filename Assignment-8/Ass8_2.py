import threading

def EvenFactor(n):
    print("Even Factor: ")
    sum_evenfact = 0
    for i in range(1,n+1):
        if n % i == 0 and i % 2 == 0:
            print(i)
            sum_evenfact += i
    print("Addition of Even Factor: ",sum_evenfact) 

def OddFact(n):
    print("Odd Factor: ")
    sum_oddfact = 0
    for i in range(1,n+1):
        if n % i == 0 and i % 2 != 0:
            print(i)
            sum_oddfact += i
    print("Addition of Odd Factor: ",sum_oddfact)  

def main():
    # num = int(input("Enter the number : "))

    print("**** Inside the Main ****")
    T1 = threading.Thread(target=EvenFactor,args=(12,))
    T1.start()
    T1.join()

    T2 = threading.Thread(target=OddFact,args=(12,))
    T2.start()
    T2.join()

    print("**** Exit the Main ****")

if __name__ == "__main__":
    main()