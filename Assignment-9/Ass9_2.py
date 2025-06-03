import multiprocessing

def SquerNum(no):
    ret = no**2
    return ret

def main():
    data = [10,20,30,40,50,60]
    result = []

    p = multiprocessing.Pool()
    result = p.map(SquerNum,data)

    p.close()
    p.join()
    
    print(result)
    
if __name__ == "__main__":
    main()