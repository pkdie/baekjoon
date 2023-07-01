# dp[i] : i에서 1를 만드는데 드는 최소 연산 횟수
# pre[i] : i에서 1로 만들 때 어떤 값으로 보내야 효율적인가

n = int(input())
dp = [0] * (10 ** 6 + 1)
pre = [0] * (10 ** 6 + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    pre[i] = i - 1
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        pre[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        pre[i] = i // 3

print(dp[n])
print(n, end=" ")

while pre[n] != 0:
    print(pre[n], end=" ")
    n = pre[n]