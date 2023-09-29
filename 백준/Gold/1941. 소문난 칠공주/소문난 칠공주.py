from collections import deque
from itertools import combinations


def bfs(x, y):
    total = 1
    deq = deque()
    deq.append((x, y))
    # 방문 위치 제거
    visited[i][j] = 0

    while deq:
        x, y = deq.popleft()

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == 1:
                # 방문한 위치 제거
                visited[ni][nj] = 0
                deq.append((ni,nj))
                total += 1
    if total == 7:
        return 1
    return 0


students = [input() for _ in range(5)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
cnt = 0
for members in combinations(range(25), 7):
    # 7공주 체크
    visited = [[0] * 5 for _ in range(5)]
    sCnt = 0
    for num in members:
        i = num // 5
        j = num % 5
        visited[i][j] = 1
        if students[i][j] == 'S':
            sCnt += 1

    if sCnt >= 4 and bfs(i, j):
        cnt += 1

print(cnt)