class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self,value):
        return self.price == value.price
    

def main():
     prod1 = Product("Laptop", 50000)
     prod2 = Product("phone", 50000)
     prod3 = Product("Tablet",20000)
     
     if prod1 == prod2:
        print("Product 1 and 2 Price is same")
     else:
        print("Product 1 and 2 price is diffrent")

     if prod1 == prod3:
        print("Product 1 and 3 Price is same")
     else:
        print("Product 1 and 3 price is diffrent")
     

if __name__ == "__main__":
    main()