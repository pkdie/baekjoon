# dp[i] : array[i]를 마지막 원소로 가지는 부분 수열의 최대 합
# 점화식 dp[i] = 모든 0<= j < i 에 대해, dp[i] = max(dp[i], dp[j] + array[i])

n = int(input())
array = list(map(int, input().split()))
dp = array[:]

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))