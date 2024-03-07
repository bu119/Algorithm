import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    wt, cnt, *num = map(int, input().split())
    dp[i] = wt
    for j in num:
        dp[i] = max(dp[i], dp[j] + wt)
print(max(dp))