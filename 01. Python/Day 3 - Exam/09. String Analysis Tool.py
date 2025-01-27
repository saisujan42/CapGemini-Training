# Checks if current character is Special Character or Not
def is_special_character(character):
    special_chars = "@#$%^&+=!"
    for char in special_chars:
        if char == character:
            return True
    return False

# Checks and returns bool value if Vowel or Not
def is_vowel(character):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        if character == vowel:
            return True
    return False

# Prints the count of vowels, consonants, digits and special characters
def print_count_of_characters(vowels, consonants, digits, special_chars):
    print(f"Vowels = {vowels}")
    print(f"Consonants = {consonants}")
    print(f"Digits = {digits}")
    print(f"Special Characters = {special_chars}")

# Counts vowels, consonants, digits, by iterating through the string
def count_and_print_characters(sentence):
    vowels = consonants = 0
    digits = special_chars = 0

    for character in sentence:
        if character.isalpha():
            if is_vowel(character):
                vowels += 1
            else:
                consonants += 1    
        elif character.isdigit():
            digits += 1
        elif is_special_character(character):
            special_chars += 1
    
    print_count_of_characters(vowels, consonants, digits, special_chars)

# Prints the Reverse of the string
def print_reverse(sentence):
    print("Reverse = ", sentence[::-1])

# takes input and returns the string
def get_input():
    sentence = input("Enter a Sentence or Word : ")
    return sentence

def main():
    sentence = get_input()
    count_and_print_characters(sentence)
    print_reverse(sentence)
main()