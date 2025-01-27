def find_sum_of_elements(arr):
    arr_sum = 0
    for i in arr:
        arr_sum += i
    return arr_sum

def get_input():
    n = int(input("Enter Size of List : "))
    arr = []

    for i in range(n):
        arr_element = int(input(f"Enter Element {i + 1} : "))
        arr.append(arr_element)
    return arr

def display_sum(arr_sum):
    print(f"Sum of List Elements : {arr_sum}")

def main():
    arr = get_input()
    arr_sum = find_sum_of_elements(arr)
    display_sum(arr_sum)
main()