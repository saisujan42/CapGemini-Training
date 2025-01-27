# Prints the Table from Start to End of range
def print_table(n, range_start, range_end):
    for i in range(range_start, range_end + 1):
        print(f"{n} * {i} = {n * i}")

# Checks if input is Float or Not to Validate Input
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False  
# Validates input and returns Float value 
def validate_input(value):
    while not is_float(value):
        print("Invalid Input.")
        value = input("Enter The Value Again : ")

    return float(value)
 
# Gets input and calls Validate Input Function
def get_input():
    value = input("Enter The Value : ")
    value = validate_input(value)

    range_start = input("Enter Start of Range : ")
    range_start = int(validate_input(range_start))   # Convert Range to Int 

    range_end = input("Enter End of Range : ")
    range_end = int(validate_input(range_end))

    return (value, min(range_start, range_end), max(range_start, range_end))  # Ensures Smaller value for start 

def main():
    (n, range_start, range_end) = get_input()
    print_table(n, range_start, range_end)
main()