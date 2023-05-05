n = int(input())
dp = [[0]*3 for _ in range(n)]
# 선택 안할 때 ,왼쪽 선택, 오른쪽 선택
# [0,0], [1,0], [0,1] 경우
dp[0] = [1, 1, 1]
for i in range(1, n):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[n-1]) % 9901)