class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_student_details():
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        gender = input("Enter Student Gender: ")
        return name, age, gender

    def display_student_details(self):
        print("Student Name: ", self.name)
        print("Student Age: ", self.age)
        print("Student Gender: ", self.gender)


class School(Student):
    def __init__(self, name, age, gender, school_name, ssc_marks):
        super().__init__(name, age, gender)
        self.school_name = school_name
        self.ssc_marks = ssc_marks

    @staticmethod
    def get_school_details():
        school_name = input("Enter School Name: ")
        ssc_marks = float(input("Enter SSC Marks: "))
        return school_name, ssc_marks

    def display_school_details(self):
        self.display_student_details()
        print("School Name: ", self.school_name)
        print("SSC Marks: ", self.ssc_marks)


class College(School):
    def __init__(self, name, age, gender, school_name, ssc_marks, college_name, college_marks):
        super().__init__(name, age, gender, school_name, ssc_marks)
        self.college_name = college_name
        self.college_marks = college_marks

    @staticmethod
    def get_college_details():
        college_name = input("Enter College Name: ")
        college_marks = float(input("Enter College Marks: "))
        return college_name, college_marks

    def display_college_details(self):
        self.display_school_details()
        print("College Name: ", self.college_name)
        print("College Marks: ", self.college_marks)


def main():
    # Get student details
    name, age, gender = Student.get_student_details()

    # Get school details
    school_name, ssc_marks = School.get_school_details()

    # Get college details
    college_name, college_marks = College.get_college_details()

    # Create a College object and display all details
    college_student = College(name, age, gender, school_name, ssc_marks, college_name, college_marks)
    college_student.display_college_details()


if __name__ == "__main__":
    main()
