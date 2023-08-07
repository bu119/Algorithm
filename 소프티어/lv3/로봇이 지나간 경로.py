import sys
from collections import deque

def bfs(i, j, d):

    visited[i][j] = 1
    deq = deque()
    deq.append((i, j, d, ''))

    while deq:
        i, j, d, order = deq.popleft()

        print(order, end='')

        # 해당 자리에서 갈 수 있는 방향 탐색
        for newD in range(4):
            ni = i + di[newD]
            nj = j + dj[newD]
            if 0 <= ni < h and 0 <= nj < w and borad[ni][nj] == '#' and not visited[ni][nj]:
                
                if newD == d:
                    ni2 = i + di[newD] *2
                    nj2 = j + dj[newD] *2

                    visited[ni][nj] = 1
                    visited[ni2][nj2] = 1

                    deq.append((ni2, nj2, d, 'A'))

                elif newD == (d-1)%4:
                    deq.append((i, j, (d-1)%4, 'L'))
                else:
                    deq.append((i, j, (d+1)%4, 'R'))


# 시작점인지 판단하기
def isStartPoint(i,j):
    cnt = 0

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < h and 0 <= nj < w and borad[ni][nj] == '#':
            cnt += 1
            dire = k
            
    if cnt == 1:
        return dire
    else:
        return 5

h, w = map(int, input().split())

# 방문했다면 '#'이고, 방문하지 않았다면 '.'
borad = [input() for _ in range(h)]

# 우하좌상
di = [0,1,0,-1]
dj = [1,0,-1,0]
direction = ['>', 'v', '<', '^']

visited = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):

        if borad[i][j] == '#':
                        
            # 시작점이 될 수 있는 지 판단
            startD = isStartPoint(i,j)

            if startD != 5:
                print(i+1, j+1)
                print(direction[startD])
                bfs(i, j, startD)
                exit()
