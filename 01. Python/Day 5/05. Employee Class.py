class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_allowances(self):
        travel_allowance = float(input("Enter Travel Allowance : "))
        food_allowance = float(input("Enter Food Allowance : "))
        rent_allowance = float(input("Enter Rental Allowance : "))

        return (travel_allowance, food_allowance, rent_allowance)
    
    def get_deductions(self):
        tax_deduction = float(input("Enter Tax Deduction : "))
        PF_deduction = float(input("Enter PF Deduction : "))
        insurance_deduction = float(input("Enter Insurance Deduction : "))

        return (tax_deduction, PF_deduction, insurance_deduction)
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def add_allowances(self, allowances):
        for allowance in allowances:
            self.__salary += allowance
    
    def add_deductions(self, deductions):
        for deduction in deductions:
            self.__salary -= deduction

def main():
    name = input("Enter Your Name : ")
    salary = float(input("Enter Your Salary : "))
    
    emp = Employee(name, salary)
    allowances = emp.get_allowances()
    deductions = emp.get_deductions()

    emp.add_allowances(allowances)
    emp.add_deductions(deductions)

    print("Gross Salary After Deductions & Allowances : ", emp.get_salary())
main()