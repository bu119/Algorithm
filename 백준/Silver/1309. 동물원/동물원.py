n = int(input())
dp = [1, 3, 7, 17]
for i in range(4, n+1):
    dp.append((dp[i-2] + dp[i-1]*2) % 9901)
print(dp[n])