from itertools import combinations
import sys
input = sys.stdin.readline


def bfs(i, j):
    stack = [(i, j)]
    visited[i][j] = 1
    cnt = 1
    virus = False
    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and graph[ni][nj] != 1:
                visited[ni][nj] = 1
                stack.append((ni, nj))
                if graph[ni][nj] == 0:
                    cnt += 1
                else:
                    virus = True
    if virus:
        return 0
    return cnt


n, m = map(int, input().split())
graph = []
candidate = dict()
wallCnt = 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for r in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for c in range(m):
        if arr[c] == 0:
            candidate[wallCnt] = (r, c)
            wallCnt += 1

ans = 0
for case in combinations(candidate, 3):
    visited = [[0]*m for _ in range(n)]
    safety = 0
    # 벽 체크
    for idx in case:
        x, y = candidate[idx]
        visited[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and visited[i][j] == 0:
                safety += bfs(i, j)

    ans = max(ans, safety)
print(ans)