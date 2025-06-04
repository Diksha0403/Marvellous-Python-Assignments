No_Power = lambda no : no**2

def main():
    try:
        num = int(input("ENter the Number: "))

        ret = No_Power(num)

        print("Power of Number: ",ret)

    except ValueError:
        print("Please enter valid integers.")

if __name__=="__main__":
    main()