# dp[i] = array[i]를 마지막 수로 하는 부분수열의 길이
# 점화식 = dp[i] = max(dp[i], dp[j] + 1), if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))
dp = [1] * 1001

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))