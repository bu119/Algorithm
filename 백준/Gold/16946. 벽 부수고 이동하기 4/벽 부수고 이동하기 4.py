import sys
input = sys.stdin.readline

def bfs(i,j):
    wall = []
    stack = []
    stack.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = 1
                if not mmap[ni][nj]:
                    cnt += 1
                    stack.append((ni,nj))
                else:
                    wall.append((ni,nj))

    for x, y in wall:
        visited[x][y] = 0
        ans[x][y] += cnt
        ans[x][y] %= 10


n, m = map(int, input().split())
mmap = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if not mmap[i][j] and not visited[i][j]:
            bfs(i, j)
        elif mmap[i][j]:
            ans[i][j] += 1
            ans[i][j] %= 10

for z in ans:
    print(''.join(map(str, z)))