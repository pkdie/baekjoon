# dp[i] : i자리의 이친수의 갯수
# dp[i] = dp[i - 2] + dp[i - 1]


n = int(input())
dp = [0] * 91
dp[1] = 1
dp[2] = 1
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])