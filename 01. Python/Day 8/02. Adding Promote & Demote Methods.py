from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def get_salary(self) -> float:
        pass

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Manager"
    
    def work(self):
        return self.role
    
    def get_salary(self):
        return self.salary

class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Developer"
    
    def work(self):
        return self.role
    
    def get_salary(self):
        return self.salary

class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Intern"
    
    def work(self):
        return self.role
    
    def get_salary(self):
        return self.salary

class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role = "Security"

    def work(self):
        return self.role
    
    def get_salary(self):
        return self.salary

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: list[Employee] = []
    
    def hire(self, employee: Employee):
        self.employees.append(employee)
        print(f"{employee.name} has been Hired.")
    
    def fire(self, employee: Employee):
        self.employees.remove(employee)
        print(f"{employee.name} has been Fired.")
    
    def get_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.get_salary()
        return total_salary

    def show_employee_details(self):
        print(f"Employees in {self.name} Department")
        for employee in self.employees:
            print(f" - {employee.name}, Salary : {employee.get_salary()}, Role : {employee.work()}")
    
    def promote(self, employee: Employee):
        if (employee.role == "Manager"):
            print("Manager Cannot be Promoted Further.")
            return
        
        elif (employee.role == "Developer"):
            print(f"{employee.name} is Promoted from Developer to Manager.")
            employee.role = "Manager"

        elif (employee.role == "Intern"):
            print(f"{employee.name} is Promoted from Intern to Developer.")
            employee.role = "Developer"
        
        elif (employee.role == "Security"):
            print(f"{employee.name} is Promoted from Security to Intern.")
            employee.role = "Intern"

        employee.salary += 10000    

    def demote(self, employee: Employee):
        if (employee.role == "Manager"):
            print(f"{employee.name} is Demoted from Manager to Developer.")
            employee.role = "Developer"
        
        elif (employee.role == "Developer"):
            print(f"{employee.name} is Demoted from Developer to Intern.")
            employee.role = "Intern"
        
        elif (employee.role == "Intern"):
            print(f"{employee.name} is Demoted from Intern to Security.")
            employee.role = "Security"            

        elif (employee.role == "Security"):
            print("Secuirty cannot be Further Demoted.")
            return
        
        employee.salary -= 10000
        
def main():
    manager = Manager("Alice", 50000)
    developer = Developer("Bob", 40000)
    intern = Intern("Charlie", 30000)
    security = Security("Ram", 20000)

    it_department = Department("IT")

    it_department.hire(manager)
    it_department.hire(developer)
    it_department.hire(intern)
    it_department.hire(security)

    it_department.show_employee_details()

    total_salary = it_department.get_total_salary()
    print(f"Total Salary of {it_department.name} : {total_salary}")

    it_department.promote(manager)
    it_department.promote(developer)

    it_department.demote(security)
    it_department.demote(developer)
main()