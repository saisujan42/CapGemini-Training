import sys
def find_min_max(arr):
    min_element = int('inf')
    max_element = int('-inf')

    for i in arr:
        min_element = min(i, min_element)
        max_element = max(i, max_element)
    
    return (min_element, max_element)

def get_input():
    n = int(input("Enter Size of List : "))
    arr = [int(input(f"Enter Element {i + 1} : ")) for i in range(n)]
    return arr

def display(min_element, max_element):
    print("Minimum Element : ", min_element)
    print("Maximum Element : ", max_element)

def main():
    arr = get_input()
    (min_element, max_element) = find_min_max(arr)
    display(min_element, max_element)

main()