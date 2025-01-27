def print_array(arr):
    print("The Array Elements are : ")
    for i in arr:
        print(i, end = ' ')

def get_input():
    n = int(input("Enter Size of Array : "))
    arr = []

    for i in range(n):
        ip = input(f"Enter Data {i + 1}: ")
        arr.append(ip)

    return arr

def main():
    arr = get_input()
    print_array(arr)
main()