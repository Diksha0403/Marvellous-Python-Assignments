class Arithmatic:
    def __init__(self):
        self.val1 = 0
        self.val2 = 0

    def Accept(self):
        self.val1 = int(input("Enter the first Number: "))
        self.val2 = int(input("Enter the second Number: "))

    def Addition(self):
        ans = 0
        ans = self.val1 + self.val2
        return ans

    def Substraction(self):
        ans = 0
        ans = self.val1- self.val2
        return ans

    def Multiplication(self):
        ans = 0
        ans = self.val1 * self.val2
        return ans

    def Division(self):
        ans = 0
        ans = self.val1/ self.val2
        return ans

def main():
    
    obj = Arithmatic()
    obj.Accept()

    ret = obj.Addition()
    print("Addition: ", ret)

    ret = obj.Substraction()
    print("Substraction: ", ret)

    ret = obj.Multiplication()
    print("Multiplication: ", ret)

    ret = obj.Division()
    print("Division: ", ret)



if __name__=="__main__":
    main()