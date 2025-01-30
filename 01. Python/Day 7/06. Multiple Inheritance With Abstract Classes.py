from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Person, Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        print("Manager Name : ", self.name)
    
    def get_salary(self):
        print("Manager Salary : ", self.salary)

def main():
    manager = Manager("John", 50000)
    manager.get_name()
    manager.get_salary()
main()