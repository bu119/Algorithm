import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 기간당 최대 페이지 수 저장
dp = [[0]*(n+1) for _ in range(m+1)]

# 챕터 당 시간과 양
for i in range(1, m+1):
    # 기간, 양
    w, v = map(int, input().split())
    # 기간 별 최대량
    for j in range(1, n+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
print(dp[m][n])