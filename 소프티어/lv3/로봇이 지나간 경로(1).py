import sys
from collections import deque

# 명령어 찾기
def bfs(i, j, d):

    visited[i][j] = 1
    deq = deque()
    # 현재 행, 열, 방향, 현재까지 명령어, 이전 명령어
    deq.append((i, j, d, '', ''))

    while deq:
        i, j, d, order, pre = deq.popleft()
		
        # 모든 경로를 방문
        if passRoad == visited[i][j]:
            return order
        
        for now in ['A','L','R']:

            if now == 'A':
                # 로봇이 바라보는 방향으로 두 칸 전진한다.
                ni1 = i + di[d]
                nj1 = j + dj[d]
                
                ni2 = i + di[d]*2
                nj2 = j + dj[d]*2

                if 0 <= ni2 < h and 0 <= nj2 < w and borad[ni1][nj1] == '#' and not visited[ni1][nj1]:
                    visited[ni1][nj1] = visited[i][j] + 1
                    visited[ni2][nj2] = visited[i][j] + 2

                    deq.append((ni2, nj2, d, order+now, now))
            
            elif now == 'L' and pre != 'R':
            	# 왼쪽 회전
                deq.append((i, j, (d-1)%4, order+now, now))

            elif now == 'R' and pre != 'L':
            	# 오른쪽 회전
                deq.append((i, j, (d+1)%4, order+now, now))


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
borad = []
# 방문 가능한 경로 수 저장 
passRoad = 0
for _ in range(h):
    arr = input() 
    borad.append(arr)
    passRoad += arr.count('#')

# 우하좌상
di = [0,1,0,-1]
dj = [1,0,-1,0]
direction = ['>', 'v', '<', '^']
# 방문체크
visited = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):

        if borad[i][j] == '#':
                        
            # 시작점이 될 수 있는 지 판단
            startD = isStartPoint(i,j)
            # 시작점 이면
            if startD != 5:
                order = bfs(i, j, startD)
                print(i+1, j+1)
                print(direction[startD])
                print(order)
                exit()
