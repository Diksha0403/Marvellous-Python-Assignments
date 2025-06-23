class Book:
    def __init__(self,price):
        self.__Price = price

    def get(self):
        return self.__Price

    def set(self,new_price):
        if new_price >= 0:
            self.__Price = new_price
            return new_price


def main():
    obj1 = Book(200)

    rate = obj1.get()

    print("Original Price:", rate)  

    obj1.set(500)  
    print("Updated Price:", obj1.get())


if __name__ == "__main__":
    main()