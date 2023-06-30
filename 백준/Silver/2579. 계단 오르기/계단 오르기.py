# dp[i][j] = 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때 점수 합의 최댓값, 단 i번째 계단은 반드시 밟아야함. j가 3 이상일수는 없다
# dp[k][1] = max(dp[k - 2][1], dp[k - 2][2]) + S[k] S[k]는 k번째 계단에 쓰여 있는 점수
# dp[k][2] = dp[k - 1][1] + S[k]

n = int(input())
dp = [[0, 0, 0] for _ in range(301)]
s = [0] * (301)

for i in range(1, n + 1):
    s[i] = int(input())

dp[1][1] = s[1]
dp[2][1] = s[2]
dp[2][2] = s[1] + s[2]

for i in range(3, n + 1):
    for j in range(1, 3):
        if j == 1:
            dp[i][j] = max(dp[i - 2][1], dp[i -2][2]) + s[i]
        if j == 2:
            dp[i][j] = dp[i - 1][1] + s[i]

print(max(dp[n][1], dp[n][2]))