coins = {}
N = int(input())
for i in range(N):
    coin = int(input())
    if coin in coins:
        coins[coin] += 1
    else:
        coins[coin] = 1

for coin, freq in coins.items():
    print(f"{coin} {freq}")