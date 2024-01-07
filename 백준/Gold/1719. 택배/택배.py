import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [[2000000001]*(n+1) for _ in range(n+1)]
# 첫번째 집하장 저장
firstPath = [['-']*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = c
    dist[b][a] = c
    firstPath[a-1][b-1] = b
    firstPath[b-1][a-1] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        if i == k:
            continue
        for j in range(1, n+1):
            if j == k or i == j:
                continue
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                # 첫번째 집하장 저장
                firstPath[i-1][j-1] = firstPath[i-1][k-1]

for i in range(n):
    print(*firstPath[i])