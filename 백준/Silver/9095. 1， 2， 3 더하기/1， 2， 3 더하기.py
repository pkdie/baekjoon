# 문제아이디어는 dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]라는 점화식

for tc in range(int(input())):
    n = int(input())
    dp = [0] * max(4, n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])