def compare(max_val, x, variable, ch):
    if x > max_val:
        return (ch, x)
    return (variable, max_val)

def get_input_and_compare():
    max_val = -1
    variable = ""
    
    a = int(input("Enter 1st Number: "))
    (variable, max_val) = compare(max_val, a, variable, "a")

    b = int(input("Enter 2nd Number: "))
    (variable, max_val) = compare(max_val, b, variable, "b")

    c = int(input("Enter 3rd Number: "))
    (variable, max_val) = compare(max_val, c, variable, "c")

    return (variable, max_val)

def display(variable, max_val):
    print(f"Max Value {variable} = {max_val}")

def main():
    (ch, max_val) = get_input_and_compare()
    display(ch, max_val)
main()