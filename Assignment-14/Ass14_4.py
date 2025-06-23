class School:
    school_name = "Marvellous"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def StudentInfo(self):
        print("Student Roll Number: ",self.roll_no)
        print("Student Name: ",self.name,"\n" )

    @classmethod
    def SchoolDetails(cls):
        cls.school_name = "Marvellous Infosys"
        print("New School Name: "+cls.school_name,"\n")


def main():
    print("\nOld School Name: ",School.school_name,"\n")

    stud1 = School("Rohit",101)
    stud2 = School("pooja",102)

    stud1.StudentInfo()
    stud2.StudentInfo() 

    print("------------------------------------\n")

    School.SchoolDetails()

    stud1.StudentInfo()
    stud2.StudentInfo() 



if __name__ == "__main__":
    main()