import time
import threading
import multiprocessing

def NormalFun(num):
    total = 0
    for i in range(1,num+1):
        total += i 
    return total

def ThreadFun(num):
    total = 0
    for i in range(1,num+1):
        total += i 
    print("Threading Sum: ",total) 

def ProcessFun(num):
    total = 0
    for i in range(1,num+1):
        total += i 
    print("Processing Sum: ",total) 



def main():
    no = 10000000
    start = time.time()
    ret1 = NormalFun(no)
    print("Normal Sum:", ret1)
    print("Normal Function Time:", time.time() - start, "seconds\n")

    T1 = threading.Thread(target=ThreadFun,args=(no,))
    T1.start()
    T1.join()
    print("Threading Time:", time.time() - start, "seconds\n")

    p = multiprocessing.Pool()
    result = p.map(ProcessFun,[no])
    p.close()
    p.join()
    
    print("MultiProcessing Time:", time.time() - start, "seconds\n")


if __name__ == "__main__":
    main()
