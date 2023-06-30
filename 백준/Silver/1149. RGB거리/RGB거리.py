# 테이블 정의 dp[i][j] : i번째 집에서 j색깔을 칠했을때 든 최소 비용 j == 1: 빨간색 j == 2: 초록색 j == 3: 파란색
# 점화식 dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j + 1]) + dp[i][j]


n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = list(map(int, input().split()))

for i in range(2, n + 1):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][j]
        if j == 1:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][j]
        if j == 2:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + dp [i][j]

print(min(dp[n]))