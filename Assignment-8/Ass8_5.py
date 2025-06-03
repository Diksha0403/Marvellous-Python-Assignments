import threading

def Thread1():
    print("*** Start Thread-1 ***")
    for i in range(1,51):
        print(i,end=" ")
    print("*** Exit from Thread-1 ***")

def Thread2():
    print("*** Start Thread-2 ***")
    for i in range(50,0,-1):
        print(i,end=" ")
    print("*** Exit from Thread-2 ***")
        
def main():
    print("**** Inside the Main ****")
    T1 = threading.Thread(target=Thread1)
    T1.start()
    T1.join()

    T2 = threading.Thread(target=Thread2)
    T2.start()
    T2.join()

    print("**** Exit the Main ****")


if __name__ == "__main__":
    main()