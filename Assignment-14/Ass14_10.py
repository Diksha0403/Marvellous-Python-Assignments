class Employee:
    def __init__(self,name,department,salary):
        self.name = name 
        self._department = department
        self.__salary = salary

def main():
    emp1 = Employee("Rohit","Development",50000)

    print("Employee name : "+emp1.name)
    print("Employee department : "+emp1._department)
    print("Employee salary : ",emp1._Employee__salary)


if __name__ == "__main__":
    main()

    
