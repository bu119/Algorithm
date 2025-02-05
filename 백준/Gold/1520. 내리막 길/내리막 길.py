import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):
    if i == m-1 and j == n-1:
        return 1
    if visited[i][j] != -1:
        return visited[i][j]

    visited[i][j] = 0   # 방문 체크
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < m and 0 <= nj < n and rectangle[ni][nj] < rectangle[i][j]:
            visited[i][j] += dfs(ni, nj)
            
    return visited[i][j]


m, n = map(int, input().split())
rectangle = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1]*n for _ in range(m)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

print(dfs(0, 0))