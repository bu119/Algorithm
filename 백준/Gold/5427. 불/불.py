from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global deq, visited, building
    # 상근이 위치는 뒤에 놓기
    deq.append((x, y))
    visited[x][y] = 1
    while deq:
        x, y = deq.popleft()

        # 사람이 탈출 하면
        if visited[x][y] > 0 and (x in {0, h-1} or y in {0, w-1}):
            return visited[x][y]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.' and visited[nx][ny] == 0:
                deq.append((nx, ny))

                if visited[x][y] == -1:
                    visited[nx][ny] = -1
                    building[nx][ny] = '*'
                else:
                    visited[nx][ny] = visited[x][y] + 1

    return 'IMPOSSIBLE'


t = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(t):
    w, h = map(int, input().split())
    building = []
    deq = deque()
    # 불, 사람, 다 방문 체크 (불 난데 사람 못가고, 갔는데 안가는 거는 똑같음)
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        row = list(input())
        building.append(row)
        for j in range(w):
            if row[j] == "*":
                deq.append((i, j))
                visited[i][j] = -1
            elif row[j] == '@':
                sgi, sgj = i, j
                # 상근이 위치를 저장하고 빈 공간으로 변경
                building[i][j] = '.'
    print(bfs(sgi, sgj))