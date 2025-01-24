def get_input():
    n = int(input("Enter N Value: "))
    arr = []

    for i in range(n):
        temp = int(input(f"Enter Number {i + 1}: "))
        arr.append(temp)
    
    return (n, arr)

def calculate_sum(n, arr):
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum

def calculate_average(n, arr):
    return calculate_sum(n, arr) / n

def display(n, avg):
    print(f"The Average of {n} Numbers Is : {avg}")

def main():
    (n, arr) = get_input()
    avg = calculate_average(n, arr)
    display(n, avg)

main()