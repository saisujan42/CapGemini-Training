
# Checks if Input of Size of Array given is Valid 
def check_size(n):
    while not n.isdigit() or int(n) < 0:
        print("Invalid Input. Enter Non-Negative Integer Value.")
        n = input("Enter Size of List of Numbers: ")

    return int(n)

# Checks if Input of Array Element given is Valid or Not 
def check_value(n, i):
    while not n.isdigit() or int(n) < 0:
        print("\nInvalid Input. Enter Non-Negative Integer Value. ")
        n = input(f"Enter Number {i + 1} : ")
    
    return int(n)

# Prints Odd and Even Elements
def display(even, odd):
    print("\nEven Numbers: ")
    for number in even:
        print(number, end = ' ')
    
    print("\nOdd Numbers: ")
    for number in odd:
        print(number, end = ' ')

# Takes and Input and validates input format
# Also Appends Odd and Even Elements into Seperate Arrays
def get_input_and_seperate():
    n = input("Enter Size of List of Numbers: ")
    n = check_size(n)                                           # Checks for Valid Input and Returns Integer Value

    even = []
    odd = []

    for i in range(n):
        value = input(f"Enter Number {i + 1} : ")
        value = check_value(value, i)

        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)
    return (odd, even)

def main():
    (odd, even) = get_input_and_seperate()
    display(odd, even)
main()