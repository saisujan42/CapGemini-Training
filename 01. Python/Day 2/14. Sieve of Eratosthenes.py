def PrintPrimes(n):
    isPrime = [True for i in range(n + 2)]
    isPrime[0] = isPrime[1] = False

    for i in range(2, n + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    
    return isPrime

def PrintAnswer(n, ans):
    for i in range(n):
        if ans[i]:
            print(i)

def main():
    n = int(input("Enter Max Value for Range: "))
    ans = PrintPrimes(n)
    PrintAnswer(n, ans)
main()