def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    ret = 0

    print("Enter the values")

    for i in range(size):
        no = int(input())
        data.append(no)

    print("Addition of elements of the list is : ")
    for value in data:
        ret += value
    print(ret)

if __name__ == "__main__":
    main()