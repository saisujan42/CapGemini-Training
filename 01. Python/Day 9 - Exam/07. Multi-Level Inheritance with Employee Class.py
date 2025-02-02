class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        super().display_info()
        print("Employee ID: ", self.employee_id)
        print("Department: ", self.department)

class Manager(Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size

    def approve_leave(self, employee_name, days):
        print(f"Manager {self.name} has approved {days} days of leave for {employee_name}.")

    def display_info(self):
        super().display_info()
        print("Team Size : ", self.team_size)

person = Person("Alice", 30)
employee = Employee("Bob", 35, "E123", "IT")
manager = Manager("Charlie", 40, "M456", "HR", 10)

person.display_info()
employee.display_info()
manager.display_info()

manager.approve_leave("Bob", 5)