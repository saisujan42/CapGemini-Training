# Prints Strong or Weak if All Conditions are Met
def print_strong_or_not(uppercase, lowercase, digits, special_characters):
    if uppercase > 0 and lowercase > 0 and digits > 0 and special_characters > 0:
        print("Your Password is Strong")
    else:
        print("Your Password is Weak")

# Checks if the current character is a Special Character or Not
def special_character_or_not(character):
    special_chars = "@#$%^&+=!"
    for char in special_chars:
        if character == char:
            return True
    return False

# Firstly, Checks for Password Size
# Then Counts the Uppercase, Lowercase, Digits and special characters 
def check_password_strength(password):
    if len(password) < 8:
        print("Passwors is Weak")
    else:
        uppercase = lowercase = 0
        digits = special_characters = 0

        for character in password:
            if special_character_or_not(character):
                special_characters += 1
            elif character.isdigit():
                digits += 1
            elif character.isalpha():
                if character.isupper():
                    uppercase += 1
                else:
                    lowercase += 1
        print_strong_or_not(uppercase, lowercase, digits, special_characters)

# Reads a string as input
def get_input():
    password = input("Enter Password : ")
    return password

def main():
    password = get_input()
    check_password_strength(password)
main()