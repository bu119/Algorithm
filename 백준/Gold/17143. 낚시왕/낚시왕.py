import sys
input = sys.stdin.readline

def move_shark():
    ocean = [[[] for _ in range(c)] for _ in range(r)]
    # 전체 상어 이동
    for row in range(r):
        for col in range(c):
            if sea[row][col]:
                z, s, d = sea[row][col][0]
                x = row
                y = col
                go = 0
                # 상어 속도 만큼 이동
                while go < s:
                    nx = x + di[d]
                    ny = y + dj[d]
                    if 0 <= nx < r and 0 <= ny < c:
                        x, y = nx, ny
                        go += 1
                    # 벽과 충돌, 방향전환
                    else:
                        d = boundary[d]
                        continue
                ocean[x][y].append((z, s, d))
    return ocean


def shark_eat():
    global sea
    for row in range(r):
        for col in range(c):
            # 한 칸에 상어가 2마리 이상 있는 경우
            if 1 < len(sea[row][col]):
                sea[row][col].sort(reverse=True)
                sea[row][col] = [sea[row][col][0]]


def catch_shark(j):
    global sea
    # 행 탐색
    for i in range(r):
        if sea[i][j]:
            # 상어를 잡는다.
            z, s, d = sea[i][j].pop()
            return z
    return 0


# 격자판의 크기 R, C와 상어의 수 M
r, c, m = map(int, input().split())
sea = [[[] for _ in range(c)] for _ in range(r)]

# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
boundary = {1:2, 2:1, 3:4, 4:3}

for _ in range(m):
    # (rr, cc)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
    rr, cc, s, d, z = map(int, input().split())
    sea[rr-1][cc-1].append((z, s, d))

fishing = 0
for j in range(c):
    # 낚시
    fishing += catch_shark(j)
    # 상어가 이동한다.
    sea = move_shark()
    # 큰 상어가 먹는다
    shark_eat()
print(fishing)