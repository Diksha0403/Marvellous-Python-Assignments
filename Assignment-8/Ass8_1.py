import threading

def Even():
    print("First 10 Even number: ")
    for i in range(1,20):
        if (i % 2 ==0):
            print(i)
            

def Odd():
    print("First 10 Odd number: ")
    for i in range(1,20):
        if (i % 2 != 0):
            print(i)
            

def main():
    print("Inside the Main")
    T1 = threading.Thread(target=Even)
    T1.start()
    T1.join()

    T2 = threading.Thread(target=Odd)
    T2.start()
    T2.join()

    print("End the Main")
        

if __name__ == "__main__":
    main()