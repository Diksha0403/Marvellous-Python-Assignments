class Calculator:
    def __init__(self,A,B):
        self.A = A
        self.B = B

    def Addition(self):
        Ans = 0
        Ans = self.A + self.B
        return Ans
    
    def Subtract(self):
        Ans = 0
        Ans = self.A - self.B
        return Ans

    def Multiplay(self):
        Ans = 0
        Ans = self.A * self.B
        return Ans

    def Divide(self):
        Ans = 0
        Ans = self.A / self.B
        return Ans

def main():
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number: "))

    obj = Calculator(num1,num2)

    print("Addition: ",obj.Addition())
    print("Subtract: ",obj.Subtract())
    print("Multiply: ",obj.Multiplay())
    print("Divide: ",obj.Divide())


if __name__ == "__main__":
    main()