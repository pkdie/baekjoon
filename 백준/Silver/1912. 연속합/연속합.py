# dp[i] : 연속된 i번째 수

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    dp[i] = max(dp[i], dp[i - 1] + dp[i])

print(max(dp))