def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter The Number: "))
    print(isPrime(n))
main()