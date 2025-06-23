class Vehicle:
    def start(self):
        print("Vehical is Start \n")

    
class Car(Vehicle):
    def start(self):
        print("Car is Start")

def main():
    obj1 = Vehicle()
    obj2= Car()

    print("\nThis Start methd from class Vehicle: ", end=" ")
    obj1.start()

    print("This Start methd from class Car: ",end=" ")
    obj2.start()


if __name__ == "__main__":
    main()
