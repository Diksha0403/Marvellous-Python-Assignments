
def Add(no1,no2):
    ans = no1 + no2
    return ans

def main():
    print("Input: ")
    val1=int(input())
    
    val2=int(input())

    Result = Add(val1,val2)
    print("Addition is: ",Result)

    
if __name__ == "__main__":
    main()