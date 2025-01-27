def print_fibonacci(n):
    a = 0
    b = 1
    print(a, b, end = ' ')
    for i in range(3, n + 1):
        c = a + b
        print(c, end = ' ')
        a = b
        b = c

def get_input():
    n = int(input("Enter Size of Series : "))
    return n

def main():
    n = get_input()
    print_fibonacci(n)
main()
