import sys
input = sys.stdin.readline

# 빙산 덩어리 개수 구하기
def bfs(x,y):
    ice = []
    stack = [(x,y)]
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()

        for z in range(4):
            nx = x + di[z]
            ny = y + dj[z]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if sea[nx][ny] > 0:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))
                # 빙산 녹이기
                elif sea[x][y]:
                    sea[x][y] -= 1
        # 존재하는 빙산 인덱스
        if sea[x][y] > 0:
            ice.append((x,y))
    return ice


n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
ans = 0
iceberg = 0
flag = 1

visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if sea[i][j] and visited[i][j] == 0:
            iceberg += 1
            ice = bfs(i, j)

while iceberg < 2 and flag:
    visited = [[0] * m for _ in range(n)]
    # 빙산 개수 리셋
    iceberg = 0
    flag = 0
    for r, c in ice:
        if sea[r][c] and visited[r][c] == 0:
            iceberg += 1
            ice = bfs(r, c)
            flag = 1
    # 1년 지남
    ans += 1

if iceberg < 2:
    ans = 0

print(ans)