n = int(input())
wines = [int(input()) for _ in range(n)]

dp = [0]*n
dp[0] = wines[0]

if n > 1:
    dp[1] = wines[0] + wines[1]

if n > 2:
    # 지금 안먹기, 직전꺼 안먹기, 전전꺼 안먹기
    dp[2] = max(dp[1], dp[0] + wines[2], wines[1] + wines[2])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])

print(dp[n-1])