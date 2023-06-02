import sys
input = sys.stdin.readline

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]
    
for j in range(3, 10001):
    dp[j] += dp[j-3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])