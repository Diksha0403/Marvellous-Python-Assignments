import threading
import time

def Number(name):
    for i in range(1,6):
        print(name,i)
        time.sleep(1)
       


def main():
    T1 = threading.Thread(target=Number,args=("Thread-1",))
     
    T2 = threading.Thread(target=Number,args=("Thread-2",))
   
    T3 = threading.Thread(target=Number,args=("Thread-3",))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    
    

if __name__=="__main__":
    main()