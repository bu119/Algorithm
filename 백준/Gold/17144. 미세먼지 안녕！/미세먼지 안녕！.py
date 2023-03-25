import sys
input = sys.stdin.readline

# 먼지 퍼트리기
def spreadDust():
    global dust

    while dust:
        x, y, v = dust.pop()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < r and 0 <= ny < c and room[nx][ny] > -1:
                room[nx][ny] += (v // 5)
                room[x][y] -= (v // 5)

#공기청정기돌리기
def operateCleaner(dir):
    global cleaner
    # 기계 위치
    if dir == 'up':
        dix = dx
        djy = dy
        x, y = cleaner[0]
        sx, ex = 0, x
        x -= 1
    else:
        dix = di
        djy = dj
        x, y = cleaner[1]
        sx, ex = x, r-1
        x += 1

    # 방향
    k = 0
    while k < 4:
        nx = x + dix[k]
        ny = y + djy[k]
        if sx <= nx <= ex and 0 <= ny < c:
            if room[nx][ny] == -1:
                room[x][y] = 0
                return
            room[x][y] = room[nx][ny]
            x, y = nx, ny
        else:
            k += 1


r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

# 위 순환 - 시계로 먼지 이동 저장
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 아래순환 - 반시계로 먼지 이동 저장
di = [1,0,-1,0]
dj = [0,1,0,-1]

# 기계 위치
cleaner = []
for tc in range(t):
    # 먼지가 있는 위치 찾기
    dust = []
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                dust.append((i, j, room[i][j]))
            if room[i][j] == -1 and tc == 0:
                cleaner.append((i, j))
    # 먼지 퍼트리기
    spreadDust()
    # print(room)
    # 기계 작동
    operateCleaner('up')
    operateCleaner('down')
    # print(room)
    # print()

ans = 2
for z in room:
    ans += sum(z)

print(ans)