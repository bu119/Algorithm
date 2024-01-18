from collections import deque

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    deq = deque()
    deq.append((x, y))
    while deq:
        x, y = deq.popleft()

        if x == x2 - 1 and y == y2 - 1:
            return visited[x][y]

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]
                if graph[nx][ny] == '0':
                    deq.appendleft((nx, ny))
                else:
                    visited[nx][ny] += 1
                    deq.append((nx, ny))


n, m = map(int, input().split())
# 주난이의 위치 x1, y1, 범인의 위치 x2, y2
x1, y1, x2, y2 = map(int, input().split())
graph = [input() for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
print(bfs(x1-1, y1-1))