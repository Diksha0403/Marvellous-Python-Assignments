

def main():
    print("Enetr 5 numbers: ")
    
    data = list()
    ret = 0
    for i in range(0,5):
        num = int(input())
        data.append(num)
        
    for value in data:
        ret = max(data)
        
    print("The Largest Number is: ",ret)
    
    # LargestNum(num)
        

if __name__ == "__main__":
    main()