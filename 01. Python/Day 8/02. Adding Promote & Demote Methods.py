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
    
    def work(self):
        return "Developer"
    
    def get_salary(self):
        return self.salary

class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    
    def work(self):
        return "Intern"
    
    def get_salary(self):
        return self.salary

class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self):
        return "Security"
    
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
main()