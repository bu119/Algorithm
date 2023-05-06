from collections import deque

n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

def bfs(i,j):
    visited = [[0] * m for _ in range(n)]

    deq = deque()
    deq.append([i, j])
    visited[i][j] = 1

    while deq:
        i, j = deq.popleft()

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                if arr[ni][nj]:
                    return visited[i][j]
                else:
                    visited[ni][nj] = visited[i][j] + 1
                    deq.append([ni,nj])

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = max(ans, bfs(i,j))
print(ans)