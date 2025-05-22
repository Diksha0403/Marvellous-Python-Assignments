def main():
    num = int(input("Enter the number: "))

    for i in range(1,11):
        ret = num * i
        print(num,"X",i,"=",ret)

if __name__ == "__main__":
    main()
    