def get_input():
    (a, b, c, d) = map(int, input("Enter 4 Space-Seperated Numbers: ").split())
    return (a, b, c, d)

def calculate_sum(a, b, c, d):
    return a + b + c + d 

def calculate_average(a, b, c, d):
    return calculate_sum(a, b, c, d) / 4

def display(avg):
    print(f"The Average of 4 Numbers Is : {avg}")

def main():
    (a, b, c, d) = get_input()
    avg = calculate_average(a, b, c, d)
    display(avg)

main()