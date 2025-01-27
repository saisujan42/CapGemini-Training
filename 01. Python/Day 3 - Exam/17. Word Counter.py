import re

# Iterating Through Dictionary to Print Word Count
def print_occurrences(word_count):
    for word, count in word_count.items():
        print(f"{word} = {count}")
        
# Splitting String into Words Using Split
# Using Dictionary to Count Words
def count_and_print_occurrences(str):
    word_count = {}
    str = re.split(r"[ ,.:;?!#0-9]+", str)      # Using Regular Expressions to Split Sentence
                                                # Removes Spaces, Commas, FullStops, Digits, etc.
    for word in str:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print_occurrences(word_count)

# Takes String as Input and returns
def get_input():
    str = input("Enter A Sentence: ")
    return str

def main():
    str = get_input()
    count_and_print_occurrences(str)
main()