class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def DisplayPerson(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

    def DisplayTeacher(self):
        self.DisplayPerson()
        print("Subject: ",self.subject)
        print("Salary: ",self.salary)

def main():
    obj1 = Teacher("Devid",35,"Python",350000)
    obj1.DisplayTeacher()

if __name__=="__main__":
    main()


