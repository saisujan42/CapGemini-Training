class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

    def get_student_details(self):
        self.name = input("Enter Student Name: ")
        self.age = int(input("Enter Student Age: "))
        self.gender = input("Enter Student Gender: ")

    def display_student_details(self):
        print("\nStudent Details ")
        print("Student Name: ", self.name)
        print("Student Age: ", self.age)
        print("Student Gender: ", self.gender)

class School(Student):
    def __init__(self):
        super().__init__()
        self.school_name = ""
        self.ssc_marks = 0

    def get_school_details(self):
        self.school_name = input("Enter School Name: ")
        self.ssc_marks = float(input("Enter SSC Marks: "))
        

    def display_school_details(self):
        self.display_student_details()
        print("School Name: ", self.school_name)
        print("SSC Marks: ", self.ssc_marks)

class College(School):
    def __init__(self):
        super().__init__()
        self.college_name = ""
        self.college_marks = ""

    def get_college_details(self):
        self.college_name = input("Enter College Name: ")
        self.college_marks = float(input("Enter College Marks: "))

    def display_college_details(self):
        self.display_school_details()
        print("College Name: ", self.college_name)
        print("College Marks: ", self.college_marks)

def main():
    college = College()
    college.get_student_details()
    college.get_school_details()
    college.get_college_details()
    college.display_college_details()
main()