from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(i, j):
    deq = deque()
    deq.append((i,j))
    visited[i][j] = 0

    while deq:
        i, j = deq.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == -1:
                visited[ni][nj] = visited[i][j] + 1
                deq.append((ni,nj))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i,j)
        if arr[i][j] == 0:
            visited[i][j] = 0

for ans in visited:
    print(*ans)