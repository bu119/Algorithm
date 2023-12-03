n = int(input())
dp = list(range(n+1))
for i in range(2, n+1):
    for j in range(1, int(i**(1/2))+1):
        dp[i] = min(dp[i], dp[i-j*j] + 1)

print(dp[n])