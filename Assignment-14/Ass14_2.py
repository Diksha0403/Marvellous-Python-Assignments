class Rectangle:
    def __init__(self,L,W):
        self.lenght =  L
        self.width = W

    def Area(self):
        area = 0
        area = self.lenght * self.width
        return area

    def Perimeter(self):
        ret = 0
        ret = 2 * self.lenght + self.width
        return ret

def main():
    obj1 = Rectangle(10,5)
    obj2 = Rectangle(10,10)

    ret = obj1.Area()
    print("Area of Rectangle: ",ret)
    
    ret = obj2.Perimeter()
    print("Perimeter of Rectangle: ",ret)
    

if __name__ == "__main__":
    main()
