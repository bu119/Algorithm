def dfs(i, j, ssum, idx):
    global ans

    if idx == 4:
        if ans < ssum:
            ans = ssum
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, ssum + arr[ni][nj], idx + 1)
            visited[ni][nj] = 0

            # ㅜ 모양
            if idx == 2:
                visited[ni][nj] = 1
                dfs(i, j, ssum + arr[ni][nj], idx + 1)
                visited[ni][nj] = 0


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

# N×M인 종이 위에 테트로미노 하나를 놓으려고 한다.
# dfs 깊이 4 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited = [[0]*m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = 0

print(ans)