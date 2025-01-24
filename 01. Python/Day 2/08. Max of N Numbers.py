import sys

def get_input():
    n = int(input("Enter N Value: "))
    arr = []

    for i in range(n):
        temp = int(input(f"Enter Number {i + 1}: "))
        arr.append(temp)
    return (n, arr)

def find_max(n, arr):
    max_val = -1

    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

def display(n, max_val):
    print(f"The Max of {n} Numbers Is : {max_val}")

def main():
    (n, arr) = get_input()
    max_val = find_max(n, arr)
    display(n, max_val)
main()