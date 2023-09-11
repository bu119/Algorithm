import sys
input = sys.stdin.readline

def move_shark():
    # 이동한 상어 저장
    ocean = [[False]*c for _ in range(r)]
    # 전체 상어 이동
    for x in range(r):
        for y in range(c):
            if sea[x][y]:
                s, d, z = sea[x][y]
                nx = x + di[d] * s
                ny = y + dj[d] * s

                # 위아래
                if d == 1 or d == 2:
                    quota = nx // (r-1)
                    remainder = nx % (r-1)
                    # 같은 방향
                    if quota % 2 == 0:
                        nx = remainder
                    # 방향 전환
                    else:
                        d = boundary[d]
                        nx = (r - 1) - remainder
                # 좌우
                else:
                    quota = ny // (c-1)
                    remainder = ny % (c-1)
                    # 같은 방향
                    if quota % 2 == 0:
                        ny = remainder
                    # 방향 전환
                    else:
                        d = boundary[d]
                        ny = (c - 1) - remainder
                # 큰 상어만 남기기
                if not ocean[nx][ny] or ocean[nx][ny][2] < z:
                    ocean[nx][ny] = (s, d, z)
    return ocean


def catch_shark(j):
    global sea
    # 행 탐색
    for i in range(r):
        if sea[i][j]:
            # 상어를 잡는다.
            s, d, z = sea[i][j]
            sea[i][j] = False
            return z
    return 0


# 격자판의 크기 R, C와 상어의 수 M
r, c, m = map(int, input().split())
sea = [[False]*c for _ in range(r)]

# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]
boundary = {1:2, 2:1, 3:4, 4:3}

for _ in range(m):
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
    rr, cc, s, d, z = map(int, input().split())
    sea[rr-1][cc-1] = (s, d, z)

fishing = 0
for j in range(c):
    # 낚시
    fishing += catch_shark(j)
    # 상어 이동
    sea = move_shark()
print(fishing)