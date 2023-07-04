# dp[i] = i번째 날까지 상담을 진행했을 때 얻는 최대 수익
# 점화식 dp[i] =

n = int(input())
schedule = [list(map(int, input().split())) for i in range(n)]
dp = [0 for i in range(n + 1)]

for i in range(n):
    for j in range(i + schedule[i][0], n + 1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])