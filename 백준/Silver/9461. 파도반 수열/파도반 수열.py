# dp[i] = P(i)를 의미
# 점화식 dp[i] = dp[i - 1] + dp[i - 5]

t = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for _ in range(t):
    n = int(input())
    for i in range(6, n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[n])
