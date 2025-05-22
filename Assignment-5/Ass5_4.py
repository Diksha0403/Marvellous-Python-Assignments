
def main():

    no1 = int(input("Enetr first Number: "))
    no2 = int(input("Enetr second Number: "))
    no3 = int(input("Enetr third Number: "))

    if no1>=no2 and no1>=no3:
        print("The largest Numeber is:",no1)
    elif no2>=no1 and no2>=no3:
        print("The largest Numeber is:",no2)
    else:
        print("The largest Numeber is:",no3)


if __name__ == "__main__":
    main()


    