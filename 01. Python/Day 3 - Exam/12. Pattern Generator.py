# Prompts User Until Valid Input is Given
# Then Returns Integer Value of Input
def input_validity_check(n):
    while not n.isdigit() or int(n) <= 0:
        print("\nInvalid Input. Enter A Valid Positive Value.")
        n = input("Enter N Value : ")
        
    return int(n)

# Takes input and Call Validity Check fucntion
# Then returns the input
def get_input():
    n = input("Enter N Value : ")
    n = input_validity_check(n)

    choice = int(input("\nEnter \n1. To Print in Normal Order \n2. To Print in Reverse Order : "))
    return (n, choice)

# Prints in Increasing Order using Nested For Loops
def print_in_order(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end = '')
        print()

#Prints in Reverse Order Using Nested For Loops
def print_reverse(n):
    for i in range(n + 1, 1, -1):
        for j in range(1, i + 1):
            print("*", end = '')
        print()

def main():
    (n, choice) = get_input()
    if choice == 1:
        print_in_order(n)
    elif choice == 2:
        print_reverse(n)
main()