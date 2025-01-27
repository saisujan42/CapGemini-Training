import sys

# Prints the Maximum Value 
def display(max_val):
    print(f"The Maximum Value is : {max_val}")

# Compares 2 Values 
# Returns Maximum Value among it
def compare(a, b):
    if a >= b:
        return a
    return b

# Takes Input of Numbers
# Uses A Variable to Store the Max Value while Taking Input itself

def get_input_and_find_max():
    n = input("Enter Size of List of Numbers: ")

    while n <= 0:
        print("\nInvalid Input.")
        print("Enter Positive Integer.")
        n = int(input("Enter Number Of Values: "))
        
    max_val = -sys.maxsize - 1

    for i in range(n):
        num = int(input(f"Enter Number {i + 1}: "))
        max_val = compare(max_val, num)
    
    display(max_val)

def main():
    get_input_and_find_max()
main()