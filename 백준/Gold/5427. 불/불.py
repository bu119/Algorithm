from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global fire, building

    visited = [[0]*w for _ in range(h)]
    visited[x][y] = 1
    deq = deque()
    deq.append((x, y))
    while deq:
        # 퍼진 불 위치 저장
        newFire = []
        # 불 먼저 이동
        for x, y in fire:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.':
                    # 불 퍼짐
                    building[nx][ny] = '*'
                    newFire.append((nx, ny))
        fire = newFire

        # 상근이 이동
        for _ in range(len(deq)):
            x, y = deq.popleft()

            if x in {0, h-1} or y in {0, w-1}:
                return visited[x][y]

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    deq.append((nx, ny))

    return 'IMPOSSIBLE'


t = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(t):
    w, h = map(int, input().split())
    building = []
    fire = []
    for i in range(h):
        row = list(input())
        building.append(row)
        for j in range(w):
            if row[j] == "*":
                fire.append((i, j))
            elif row[j] == '@':
                sgi, sgj = i, j
                # 상근이 위치를 저장하고 빈 공간으로 변경
                building[i][j] = '.'
    print(bfs(sgi, sgj))