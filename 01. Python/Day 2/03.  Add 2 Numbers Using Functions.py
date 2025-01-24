def get_input():
    (a, b) = map(int, input("Enter 2 Numbers: ").split())
    return (a, b)

def calculate_sum(a, b):
    return a + b 

def display(sum):
    print(f"Sum Of 2 Numbers = {sum}")

def main():
    (a, b) = get_input()
    sum = calculate_sum(a, b)
    display(sum)

main()