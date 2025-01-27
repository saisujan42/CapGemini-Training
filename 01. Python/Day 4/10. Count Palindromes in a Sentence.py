# Without Using split() function

def isPalindrome(word):
    rev = word[::-1]
    if rev == word:
        return True
    return False

def count_palindromes(sentence):
    count = 0
    word = ""
    for character in sentence:
        if character.isalnum():
            word += character
        else:
            if len(word) > 0 and isPalindrome(word):
                count += 1
            word = ""
    
    if isPalindrome(word):
        count += 1
    return count

def get_input():
    sentence = input("Enter The Sentence : ")
    return sentence

def main():
    sentence = get_input()
    count = count_palindromes(sentence)
    print("Number Of Palindromes = ", count)
main()