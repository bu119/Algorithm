import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
ssum = [[0]*(n+1) for _ in range(n+1)] # 누적 합

for i in range(1,n+1):
    for j in range(1, n+1):
        ssum[i][j] = ssum[i][j-1] + ssum[i-1][j] + arr[i][j] - ssum[i-1][j-1]
# print(ssum)
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = ssum[x2][y2] - ssum[x2][y1-1] - ssum[x1-1][y2] + ssum[x1-1][y1-1]
    print(ans)