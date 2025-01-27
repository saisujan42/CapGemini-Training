#Function to Print The Answer
def display(ans):
    print(f"Factorial Value = {ans}")

#Runs a Loop from 1 to N to Calculate Factorial
def find_and_print_factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    
    display(ans)

# Takes Input Multiple Times Using While Loop
# Handles Invalid Input Cases
# Calls Another Function to Find Factorial if Input is Valid

def get_input_and_calculate():
    while True:
        print("\nPress Enter Giving Input to Exit ")
        value = input("Enter The Number: ")
        
        if value.strip() == "":                               # Exits if Enter is Pressed without Input
            print("You Have Exited Successfully")
            break

        if not value.isdigit() or int(value) < 0:                    #Prompts user to Provide Input Again
            print("Invalid Input. Enter Non-Negative Integer.")      #If non-integer values or negative values are given
            continue

        value = int(value)
        find_and_print_factorial(value)

def main():
    get_input_and_calculate()
main()