import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i,j):
    global tmp
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            tmp += 1
            dfs(ni,nj)


n, m, k = map(int, input().split())

arr = [[0]*m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

di = [0,-1,0,1]
dj = [1,0,-1,0]

visited = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            tmp = 1
            dfs(i,j)
            ans = max(ans, tmp)

print(ans)