def get_input():
    (a, b, c) = map(int, input("Enter 3 Numbers: ").split())
    return (a, b, c)

def display(max_value):
    print(f"The Max Value = {max_value}")

def find_max(a, b, c):
    if a > b and a > c:
        return a
    if b > c and b > a:
        return b
    return c

def main():
    (a, b, c) = get_input()
    max_value = find_max(a, b, c)
    display(max_value)
main()