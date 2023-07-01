# dp[i] = 2 x i 직사각형을 채우는 방법의 수                                                                                                             
# dp[i] = dp[i - 1] + (dp[i - 2] * 2)                                                                                                       
                                                                                                                                            
n = int(input())                                                                                                                            
dp = [0] * 1001                                                                                                                             
dp[1] = 1                                                                                                                                   
dp[2] = 3                                                                                                                                   
for i in range(3, n + 1):                                                                                                                   
    dp[i] = dp[i - 1] + (dp[i - 2] * 2)                                                                                                     
                                                                                                                                            
print(dp[n] % 10007)                                                                                                                        