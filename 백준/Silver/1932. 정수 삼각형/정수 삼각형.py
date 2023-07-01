# dp[i][j] : i번째 층에서 j번째 수의 여러 합 중 최대 값
# dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]

n = int(input()) # n은 삼각형의 크기
dp = [0]
for _ in range(n):
    dp.append([0] + list(map(int, input().split())))

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if j == i:
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]

print(max(dp[n]))