class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
    
    def display_info(self):
        print()
        print(f"Employee Name : {self.name}")
        print(f"Employee ID : {self.emp_id}")
        print(f"Employee Department : {self.department}")
    
    def modify_info(self):
        print()
        self.name = input("Enter New Employee Name : ")
        self.emp_id = int(input("Enter New Employee ID : "))
        self.department = input("Enter New Employee Department : ")

def main():
    name = input("Enter Employee Name : ")
    emp_id = int(input("Enter Employee ID : "))
    department = input("Enter Employee Department : ")

    emp = Employee(name, emp_id, department)

    emp.display_info()
    emp.modify_info()
    emp.display_info()
main()