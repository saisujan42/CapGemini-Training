import math

def isPrime(n):
    if n <= 1:
        return False
    
    x = int(math.sqrt(n))
    for i in range(2, x + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter The Number: "))
    print(isPrime(n))
main()