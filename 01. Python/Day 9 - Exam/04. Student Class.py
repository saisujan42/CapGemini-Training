class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    
    def student_details(self):
        print()
        print("Student Name : ", self.name)
        print("Student Roll Number : ", self.roll_number)

def main():
    student1 = Student("John", 534)
    student2 = Student("Jack", 536)

    student1.student_details()
    student2.student_details()
main()