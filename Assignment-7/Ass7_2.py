Double = lambda num : num*2

def main():

    data=list()
    
    print("Enetr the values")
    for i in range(0,5):
        no=int(input())
        data.append(no)

    print("Input Data: ",data)

    MData = list(map(Double,data))
    print("Double List: ",MData)



if __name__ == "__main__":
    main()