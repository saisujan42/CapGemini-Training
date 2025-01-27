# Checks if input is Float or Not to Validate Input
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False  

# Checks Loan Eligibiliy using if-else statements
# Prints if Loan is Approved or Denied
def check_eligibility(salary, age, credit_score):
    if salary < 30000:
        print("\nLoan Denied.")
        print("Minimum Salary of 30000 is Required")
    
    elif age < 18:
        print("\nLoan Denied.")
        print("Minimum Age of 18 is Required")
    
    elif age > 70:
        print("\nLoan Denied")
        print("Maximum Age of 70 is Only Eligible")
    
    elif credit_score < 300:
        print("\nLoan Denied.")
        print("Credit Score is Too Low.")
    
    else:
        print("\nLoan Approved.")

# Get Input and also Validate Input
def get_input_and_check_eligibility():
    salary = input("Enter Salary : ")

    while not is_float(salary):
        print("\nInvalid Input.")
        salary = input("Enter Salary : ")
    
    age = input("Enter Age : ")
    
    while not age.isdigit() or int(age) < 0:
        print("\nInvalid Input.")
        age = input("Enter Age : ")

    credit_score = input("Enter Credit Score : ")

    while not credit_score.isdigit() or int(credit_score) not in range(1, 901):
        print("\nInvalid Input. Enter Integer in Range 1-900. ")
        credit_score = input("Enter Credit Score")
    
    check_eligibility(float(salary), int(age), int(credit_score))

def main():
    get_input_and_check_eligibility()
main()