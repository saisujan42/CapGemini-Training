def display(data):
    print(f"The Area is {data}")

def get_input():
    length = int(input("Enter Length: "))
    breadth = int(input("Enter Breadth: "))
    return (length, breadth)

def calculate_area(l, b):
    return l * b

def main():
    (l, b) = get_input()
    area = calculate_area(l, b)
    display(area)

main()