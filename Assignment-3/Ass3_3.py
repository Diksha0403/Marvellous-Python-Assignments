def main():
    size = int(input("Enter the number of element: "))

    data = list()

    print("Enter the element: ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Mininum Number from the list is :")
    for val in data:
        minimum = min(data)
    print(minimum)

if __name__ == "__main__":
    main()


