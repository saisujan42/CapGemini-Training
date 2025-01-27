def isPalindrome(str):
    rev_str = str[::-1]
    if rev_str == str:
        return True
    return False

def print_answer(str_list):
    for str in str_list:
        if isPalindrome(str):
            print(str, " is a Palindrome")
        else:
            print(str, " is not a Palindrome")
    
def get_input():
    str = input("Enter String : ")
    return list(str)

def main():
    str_list = get_input()
    if isPalindrome(str_list):
        print(str_list, " is a Palindrome")
    else:
        print(str_list, " is not a Palindrome")
main()