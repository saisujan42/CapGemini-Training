# Function to Check if an Input String is Palinrome or Not
# Uses 2 Variables to Store First and Last Index of String
# Character and Start and End are Compared to Check if Same or Not
# If They are Not Same False is returned

def isPalindrome(str):
    start = 0
    end = len(str) - 1

    while start <= end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1

    return True

# Takes Input Until User Presses Enter to Exit
# Also Prints if an Input Word is Palindrome or Not

def get_input_and_check():
    while True:
        print("\nPress Enter Without Entering String to Exit ")
        
        str = input("Enter Word or Number: ")
        str = "".join(str.split())                              #To Remove Spaces from Input

        if len(str) == 0:                                       #Checks if Input Size is 0, to Exit
            print("You Have Now Exited")                 
            break
        if (isPalindrome(str)):
            print(f"{str} is a Palindrome")
        else:
            print(f"{str} is not a Palindrome")

def main():
    get_input_and_check()
main()