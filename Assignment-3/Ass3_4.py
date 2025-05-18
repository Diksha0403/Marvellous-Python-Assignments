def main():
    size = int(input("Enter the number of element: "))

    data = list()

    print("Enter the elements: ")
    for i in range(size):
        no = int(input())
        data.append(no)

    search_ele = int(input("Element to serach: "))
    for val in data:
        ret = data.count(search_ele)
    print("Frequency of element: ",ret)


if __name__ == "__main__":
    main()