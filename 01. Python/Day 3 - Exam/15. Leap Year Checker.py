# Checks if Year is Leap or Not
# 4 Multiple is a Leap Year
# But, 100 Multiple is not a Leap Year
# But, also 400 Multiple is a Leap Year
def leap_or_not(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

# Prompts User Until Valid Input is Given
# Then Returns Integer Value of Input
def input_validity_check(year):
    while not year.isdigit() or int(year) < 0:
        print("\nInvalid Input. Enter A Valid Positive Year.")
        year = input("Enter A Year : ")
        
        if year.strip() == "" :
            print("You Have Exited Successfully")
            break

    return int(year)

# Gets input until user requires
# Exits if enter is pressed
def get_input_and_validate_year():
    while True:
        print("\nPress Enter Without Giving Input to Exit.")
        year = input("Enter A Year : ")
        if year.strip() == "" :
            print("You Have Exited Successfully")
            break
        year = input_validity_check(year)

        if leap_or_not(year) == True:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")

def main():
    get_input_and_validate_year()
main()