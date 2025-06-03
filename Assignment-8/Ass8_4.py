import threading

def Small(name):
    count = 0
    for i in name:
        if i.islower():
            count += 1
    print("Small letters count is: ",count)


def Capital(name):
    count = 0
    for i in name:
        if i.isupper():
            count += 1
    print("Capital letters count is: ",count)
    

def Digital(num):
    count = 0
    for i in num:
        if i.isdigit():
            count += 1
    print("Digit number count is: ",count)


def main():
    inpt = input("Enter the Number: ")

    T1 = threading.Thread(target=Small,args=(inpt,))
    T1.start()
    T1.join()

    T1 = threading.Thread(target=Capital,args=(inpt,))
    T1.start()
    T1.join()

    T1 = threading.Thread(target=Digital,args=(inpt,))
    T1.start()
    T1.join()



if __name__ == "__main__":
    main()