import csv

class Employee:
    csv_file = "employees.csv"
    headers = ["Name", "Employee ID", "Department"]

    def __init__(self):
        with open(self.csv_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
        print("CSV File Created.")

    def write_into_csv(self, name, emp_id, department):
        with open(self.csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, emp_id, department])
    
    def display_csv_data(self):
        with open(self.csv_file, mode="r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

def main():
    employee = Employee()

    employee.write_into_csv("John", "534", "IT")
    employee.write_into_csv("Jack", "536", "HR")

    employee.display_csv_data()
main()