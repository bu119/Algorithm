import sys
input = sys.stdin.readline

# 모든 부분 격자를 시계 방향으로 90도 회전
def rotate_90():
    newBoard = [[0]*m for _ in range(m)]
    # 부분 격자
    part = 2**l
    for i in range(0, m, part):
        for j in range(0, m, part):
            for x in range(part):
                for y in range(part):
                    newBoard[i + y][j + (part-1) - x] = board[i+x][j+y]

    return newBoard

# 얼음이 있는 칸 3개 또는 그 이상과 인접해있는 지 체크
def is_3_adj_ice(x, y):
    cnt = 4
    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]
        if not (0 <= nx < m and 0 <= ny < m) or board[nx][ny] == 0:
            cnt -= 1
            if cnt < 3:
                return False
    return True

# 얼음 감소 시키기
def reduce_ice():
    newBoard = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            newBoard[i][j] = board[i][j]
            # 얼음이 있으면
            if board[i][j] == 0:
                continue
            # 3개 또는 그 이상과 인접해있지 않은 칸은 얼음 1 감소
            if not is_3_adj_ice(i, j):
                newBoard[i][j] -= 1

    return newBoard

#  남아있는 얼음의 합을 갱신하고, 현재 얼음 덩어리 크기 반환
def check_remaining_ice(i, j):
    global ice

    stack = [(i, j)]
    visited[i][j] = 1
    size = 0

    while stack:
        x, y = stack.pop()

        size += 1
        ice += board[x][y]

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < m and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] > 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))
    return size


n, q = map(int, input().split())
# 격자 크기
m = 2**n
board = [list(map(int, input().split())) for _ in range(m)]
level = list(map(int, input().split()))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
# 마법사 상어는 파이어스톰을 총 Q번 시전
for l in level:
    # 모든 부분 격자를 시계 방향으로 90도 회전
    board = rotate_90()
    # 얼음 양 줄이기
    board = reduce_ice()

ice = 0
maxSize = 0
visited = [[0] * m for _ in range(m)]
for r in range(m):
    for c in range(m):
        if board[r][c] > 0 and visited[r][c] == 0:
            # 연결되어 있는 얼음덩어리 크기
            currSize = check_remaining_ice(r, c)
            maxSize = max(maxSize, currSize)

print(ice)
print(maxSize)