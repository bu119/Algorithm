from collections import deque

def bfs(i, j):
    global cnt, size, eat
    global fish

    feed = []
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = cnt

    deq = deque()
    deq.append((i, j))

    while deq and not feed:
        for _ in range(len(deq)):
            i, j = deq.popleft()

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and space[ni][nj] <= size and not visited[ni][nj]:

                    deq.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1

                    if 0 < space[ni][nj] < size:
                        cnt = visited[ni][nj]
                        feed.append((ni, nj))       # 먹이를 먹었으면 새로운 탐색

    return feed

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 1, 0, 0]      # 상 하 좌 우
dj = [0, 0, -1, 1]

fish = [0] * 7          # 각 사이즈의 물고기 개수
size = 2
cnt = eat = 0

for i in range(n):
    for j in range(n):
        if space[i][j] and space[i][j] != 9:
            fish[space[i][j]] += 1
        if space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

# 처음 탐색
restart = bfs(x, y)

# 재 탐색
while sum(fish[1:size]) > 0 and restart:
    restart.sort()
    x = restart[0][0]
    y = restart[0][1]

    eat += 1
    fish[space[x][y]] -= 1
    space[x][y] = 0
    if size == eat:
        size += 1
        eat = 0

    restart = bfs(x, y)

print(cnt)