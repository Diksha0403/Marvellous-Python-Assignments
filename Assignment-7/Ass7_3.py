EvenNo = lambda no:(no%2==0)

def main():

    data = list()

    print("Enetr the values")
    for i in range(0,6):
        no = int(input())
        data.append(no)

    FData = list(filter(EvenNo,data))
    print("Even Number: ", FData)


if __name__ == "__main__":
    main()