import threading

def EvenList(no):
    print("Even number: ")
    sum=0
    for i in no:
        if i % 2 == 0:
            print(i)
            sum =sum + i
    print("Addition of Evenlist: ",sum)
        
            

def OddList(no):
    print("Odd number: ")
    sum = 0
    for i in no:
        if i % 2 != 0:
            print(i)
            sum = sum + i
    print("Addition of Oddlist: ",sum)
            

def main():
    print("Inside the Main")
    data = [10, 21, 32, 43, 54, 65, 76, 87]

    T1 = threading.Thread(target=EvenList,args=(data,))

    T1.start()
    T1.join()

    T2 = threading.Thread(target=OddList,args=(data,))
    T2.start()
    T2.join()

    print("End the Main")
        

if __name__ == "__main__":
    main()