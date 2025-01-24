import dis

def display():
    print("Hello World")

def multiply(a, b):
    c = a * b
    return c

def print_nos(n):
    for i in range(n):
        print(i + 1)

# Disassemble The Code to View Assembly Level Commands
def main():
    dis.dis(print_nos)
    dis.dis(multiply)
    dis.dis(display)
main()