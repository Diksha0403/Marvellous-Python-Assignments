def Palindrome(name):
    rev = ""
    for i in name:
        rev = i + rev

    if name == rev:
        print(name, "string is Palindrome")
    else:
        print(name, "string is not a Palindrome")


def main():
    String = str(input("Enetr the string: "))

    Palindrome(String)

if __name__ == "__main__":
    main()