import sys
input = sys.stdin.readline

dp = [0, 1, 2, 4, 7]

t = int(input())
n = list(int(input()) for _ in range(t))
num = max(n)

for i in range(5,num+1):
    dp.append((dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009)

for j in n:
    print(dp[j])