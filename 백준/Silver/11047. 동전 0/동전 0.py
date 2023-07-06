n, k = map(int, input().split())
coins = []
cnt = 0
for _ in range(n):
    coins.append(int(input()))

for i in range(-1, - (n + 1), -1):
    if k // coins[i] > 0:
        cnt += k // coins[i]
        k = k % coins[i]

print(cnt)