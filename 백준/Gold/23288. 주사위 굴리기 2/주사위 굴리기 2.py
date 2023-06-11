def bfs(i,j):
    global score

    visited = [[0] * m for _ in range(n)]
    stack = [(i, j)]
    num = board[i][j]
    score += num

    visited[i][j] = 1
    while stack:
        i, j = stack.pop()

        for z in range(4):
            ni = i + di[z]
            nj = j + dj[z]
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == num and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                score += board[ni][nj]
                stack.append((ni,nj))


def move(dir):
    # 주사위 위치 값 저장
    bottom, top, left, right, north, south = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    # 주사위 면 이동
    if dir == 0: # 동
        # bottom, top, left, right 자리
        dice[0], dice[1], dice[2], dice[3] = right, left, bottom, top
    elif dir == 1: # 남
        dice[0], dice[1], dice[4], dice[5] = north, south, top, bottom
    elif dir == 2: # 서
        dice[0], dice[1], dice[2], dice[3] = left, right, top, bottom
    else: # 북
        dice[0], dice[1], dice[4], dice[5] = south, north, bottom, top

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 주사위 면
# bottom, top, left, right, north, south
dice = [6,1,4,3,5,2]
# 동남서북
di = [0,1,0,-1]
dj = [1,0,-1,0]
x, y = 0, 0
score = 0
d = 0

for _ in range(k):
    nx = x + di[d]
    ny = y + dj[d]
    if 0 <= nx < n and 0 <= ny < m:
        pass
    else:
        d = (d+2) % 4
        nx = x + di[d]
        ny = y + dj[d]

    # 시작 좌표 변경
    x, y = nx, ny

    # 점수 합
    bfs(x, y)

    # 주사위 이동
    move(d)

    if dice[0] > board[x][y]:
        d = (d + 1) % 4
    elif dice[0] < board[x][y]:
        d = (d - 1) % 4

print(score)