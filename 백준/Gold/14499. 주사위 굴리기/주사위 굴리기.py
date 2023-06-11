def move(dir):
    # 주사위 면 이동
    bottom, top, left, right, north, south = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    if dir == 1: # 동
        # bottom, top, left, right 자리
        dice[0], dice[1], dice[2], dice[3] = right, left, bottom, top
    elif dir == 2: # 서
        dice[0], dice[1], dice[2], dice[3] = left, right, top, bottom
    elif dir == 3: # 북
        dice[0], dice[1], dice[4], dice[5] = south, north, bottom, top
    else:
        dice[0], dice[1], dice[4], dice[5] = north, south, top, bottom

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dk = list(map(int, input().split()))

# bottom, top, left, right, north, south
dice = [0]*6
# 동서북남
di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]

for d in dk:
    nx = x + di[d]
    ny = y + dj[d]
    if 0 <= nx < n and 0 <= ny < m:
        move(d)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[0]
        else:
            dice[0] = board[nx][ny]
            board[nx][ny] = 0
        # 시작 좌표 변경
        x, y = nx, ny
        print(dice[1])