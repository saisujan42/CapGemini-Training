import random

# Use While Loop to Take User Guesses 
# Use an if Condition to Exit if User presses Enter without input
# Prompts user to give valid input if input is out of range
# Exit if Correct Guess is given
def guess_number(correct_answer):
    while True:
        print("\nPress Enter without Input to Exit.")
        user_guess = input("Enter Your Guess : ")

        if user_guess.strip() == "":
            print("\nNice Try. Better Luck Next Time.")
            break

        while not user_guess.isdigit() or int(user_guess) <= 0 or int(user_guess) > 100:
            print("Invalid Input. Enter Integer Between 1 and 100.")
            user_guess = input("Enter Your Guess : ")
        
        if int(user_guess) == correct_answer:
            print("Correct Guess!!")
            break
        else:
            print("Wrong Guess. Try Again")

# Generate Random Number and return Value
def get_input():
    random_number = random.randint(1, 100)
    return random_number

def main():
    random_number = get_input()
    guess_number(random_number)
main()