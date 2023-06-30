# dp[i] = a[1] + a[2] + ''' + a[i] = dp[i - 1] + a[i]
# a[i] + a[i + 1] + ''' + a[j] = dp[j] - dp[i - 1]
import sys

n, m = map(int, sys.stdin.readline().split())
dp = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + dp[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j] - dp[i - 1])