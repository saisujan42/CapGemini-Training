# Using Sieve of Eratosthenes Algorithm
# Using An Array From 1 to N to Mark Indices as Prime or Not
# If A Number is Not Prime, Mark All its multiples as Not Prime Too

# Time Complexity : O(N Log(LogN))
# Space Complexity : O(Range)

# Marks Multiples as Primes
def find_primes(n):
    isPrime = [True for i in range(n + 2)]
    isPrime[0] = isPrime[1] = False

    for i in range(2, n + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    
    return isPrime

# Print the Answer
def print_primes(ans, range_start, range_end):
    for i in range(range_start, range_end + 1):
        if ans[i]:
            print(i, end = " ")

# Validate the Input and Return Int
def validate_input(value):
    while not value.isdigit() or int(value) <= 0:
        print("Invalid Input.")
        value = input("Enter The Value Again : ")

    return int(value)

# Gets input and calls Validate Input Function
def get_input():
    range_start = input("Enter Start of Range : ")
    range_start = validate_input(range_start) 

    range_end = input("Enter End of Range : ")
    range_end = validate_input(range_end)

    return (min(range_start, range_end), max(range_start, range_end))  # Ensures Smaller value for start 

def main():
    (range_start, range_end) = get_input()
    ans = find_primes(range_end)
    print_primes(ans, range_start, range_end)
main()