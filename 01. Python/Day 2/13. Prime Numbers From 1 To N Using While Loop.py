import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            return False
        i += 1
    return True

def PrintPrimes(n):
    i = 1
    while i <= n:
        if isPrime(i):
            print(i)
        i += 1

def main():
    n = int(input("Enter N Value: "))
    PrintPrimes(n)
main()