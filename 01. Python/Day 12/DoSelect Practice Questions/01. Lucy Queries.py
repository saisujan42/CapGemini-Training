def main():
    T = int(input())
    for _ in range(T):
        friends = {}
        N, Q = map(int, input().split())
        for i in range(N):
            arr = input().split()
            friends[arr[0]] = arr[1 : ]

        for q in range(Q):
            str = input()
            arr = friends[str]
            print(arr[0], end = ", ")
            print(arr[1], end = ", ")
            print(arr[2])
main()