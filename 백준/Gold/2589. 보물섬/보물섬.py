from collections import deque
import sys
input = sys.stdin.readline

# 두 보물 사이의 최단거리 찾는 함수
def bfs(i, j):
    global maxTime

    visited = [[0]*m for _ in range(l)]
    visited[i][j] = 1
    deq = deque()
    deq.append((i, j))
    while deq:
        i, j = deq.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < l and 0 <= nj < m and graph[ni][nj] == 'L' and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                deq.append((ni, nj))

    return visited[i][j] - 1


l, m = map(int, input().split())
graph = [input() for _ in range(l)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
# 최대 시간 저장
maxTime = 0
# 보물 하나의 위치 선정
for i in range(l):
    for j in range(m):
        if graph[i][j] == 'L':
            maxTime = max(maxTime, bfs(i, j))
print(maxTime)