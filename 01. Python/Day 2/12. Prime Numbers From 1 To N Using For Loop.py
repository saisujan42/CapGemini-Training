import math

def PrintPrimes(n):
    for i in range(1, n + 1):
        if isPrime(i):
            print(i)

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter N Value: "))
    PrintPrimes(n)
main()