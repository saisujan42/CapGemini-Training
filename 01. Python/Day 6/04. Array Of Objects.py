class Student:
    def __init__(self):
        (name, age) = self.get_details()
        self.name = name
        self.age = age
    
    def get_details(self):
        name = input("Enter Student Name : ")
        age = int(input("Enter Age : "))
        return name, age

    def display_details(self):
        print()
        print("Student Name : ", self.name)
        print("Student Age : ", self.age)
    
def main():
    n = int(input("Enter Number of Students : "))
    students  = []

    for i in range(n):
        students.append(Student())
    
    for i in range(n):
        students[i].display_details()
    
main()