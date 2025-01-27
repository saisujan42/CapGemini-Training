# Loops From 1 to 100
# Uses if-elif-else conditions to check if a number is multiple of 3 or 5 or both

def PrintNos():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
def main():
    PrintNos()
main()