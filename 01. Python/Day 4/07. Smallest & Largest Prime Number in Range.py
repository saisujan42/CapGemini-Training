import math
def smallest_largest_prime(primes_list):
    print("Smallest Prime in Range : ", primes_list[0])
    print("Largest Prime in Range : ", primes_list[-1])

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes_list = []

    for i in range(start, end + 1):
        if is_prime(i):
            primes_list.append(i)
    
    return primes_list

def get_input():
    range_start = int(input("Enter Start of Range : "))
    range_end = int(input("Enter End of Range : "))
    return (range_start, range_end) 

def main():
    (range_start, range_end) = get_input()
    primes_list = find_primes(range_start, range_end)
    smallest_largest_prime(primes_list)
main()