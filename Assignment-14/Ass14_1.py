class Employee:
    def __init__(self,id,name,salary):
        self.emp_id = id
        self.name = name
        self.salary = salary

def main():
    emp1 = Employee(101,"Rohit",50000)

    print("Employee ID : ",emp1.emp_id)
    print("Employee name : "+emp1.name)
    print("Employee salary : ",emp1.salary)

if __name__ == "__main__":
    main()

    