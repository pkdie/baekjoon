# dp[i][0] : fibo(i)를 호출하면 총 출력되는 0의 갯수, dp[i][1] : fibo(i)를 호출하면 총 출력되는 1의 갯수
# 점화식 dp[i][j] = dp[i - 1][j] + dp[i -2][j]

t = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for _ in range(t):
    n = int(input())
    for i in range(2, n + 1):
        for j in range(2):
            dp[i][j] = dp[i - 1][j] + dp[i - 2][j]

    print(dp[n][0], end=" ")
    print(dp[n][1])