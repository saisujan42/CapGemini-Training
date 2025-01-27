# Prints the Answer
def display(split_amount):
    print(f"Each Person Has to Pay : {split_amount}")

# Calculates the bill of each person and returns answer
def calculate_final_bill(bill_amount, no_of_people, tip_perccent):
    tip_amount = (tip_perccent / 100) * bill_amount
    final_bill = bill_amount + tip_amount
    return final_bill / no_of_people

# Checks if input is Float or Not to Validate Input
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False  

# If Invalid Input is Given, Prompts user Until Correct Input is Given
def validate_input(value):
    while not is_float(value) or float(value) < 0:
        print("\nInvalid Input.")
        value = input("Please Enter Again : ")
    
    return float(value)

# Takes Input and Calls Input Validate Function
def get_input():
    bill_amount = input("Enter Total Bill Amount : ")
    bill_amount = validate_input(bill_amount)
    
    no_of_people = input("Enter Total Number of People : ")
    no_of_people = validate_input(no_of_people)
    
    tip_percent = input("Enter Tip Percentage (0 - 100%) : ")
    tip_percent = validate_input(tip_percent)

    return (bill_amount, no_of_people, tip_percent)

def main():
    (bill, people, tip) = get_input()
    split_amount = calculate_final_bill(bill, people, tip)
    display(split_amount)

main()