import sys
input = sys.stdin.readline

t = int(input())

# 가장 작은 수
# dp 활용
dp = ['9'*17]*101
dp[2] = '1'
dp[3] = '7'
dp[4] = '4'
dp[5] = '2'
dp[6] = '0'
dp[7] = '8'
dp[8] = '10'
dp[9] = '18'
dp[10] = '22'

for i in range(11, 101):
    dp[i] = int(dp[i])
    for j in range(2, 8):
        dpIJ = dp[i-j]
        if dpIJ == '0':
            dpIJ = '6'
        dp[i] = min(int(dp[i]), int(dpIJ + dp[j]))
    dp[i] = str(dp[i])

for _ in range(t):
    n = int(input())

    # 가장 큰 수
    if n % 2 == 0:
        maxNum = (n // 2) * '1'
    else:
        maxNum = '7' + (n // 2 - 1) * '1'

    # 가장 작은 수
    minNum = dp[n]
    if n == 6:
        minNum = 6

    print(minNum, maxNum)