# 0세대는 주어진 선
# 1세대는 0세대를 90도 회전후 연결한 2개로 이루어진 선
# 2세대는 1세대를 90도 회전후 연결한 4개로 이루어진 선

# 기존 선을 90도 회전하는 위치 저장 함수
def move_90(last_i, last_j):
    global move_d
    # 시작점을 마지막 지점으로 설정하고
    # 처음 이동 방향에 - 1을 해서 다시 이동하면 된다.
    # -1 하면 시계 방향이 된다. (아니면 이동 방향을 저장)

    m = len(move_d)
    for z in range(m-1,-1,-1):
        # k값 0, 1, 2, 3으로 나오게 변경
        md = (move_d[z]+1) % 4
        # 변경된 위치값
        ni = last_i + di[md]
        nj = last_j + dj[md]
        if 0 <= ni <= 100 and 0 <= nj <= 100:
            # 방문 체크
            board[ni][nj] = 1
            move_d.append(md)
            last_i = ni
            last_j = nj
        else:
            break

    return last_i, last_j


# 정사각형인지 판별하는 함수
def find_square(r, c):
    for k in range(3):
        r += di[k]
        c += dj[k]
        if 0 <= r <= 100 and 0 <= c <= 100 and board[r][c]:
            pass
        else:
            return False

    return True


n = int(input())
board = [[0] * 101 for _ in range(101)]
# 동북서남
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

# x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
for _ in range(n):
    # x축(열) = j, y축(행) = i
    j, i, d, g = map(int, input().split())
    # 방문 체크
    board[i][j] = 1
    # 이동 방향 저장
    move_d = [d]
    # 이동 위치
    last_i = i + di[d]
    last_j = j + dj[d]
    # 이동 방문 체크
    board[last_i][last_j] = 1

    # g+1번 반복 (0세대부터 g세대까지)
    # d-1을 해주면서 반복
    for _ in range(g):
        # 현재 선 모양을 시계방향 90도 회전하여
        # 연결한 위치와 방향을 추가해주는 함수
        last_i, last_j = move_90(last_i, last_j)

        # 시행 횟수 감소
        g -= 1

ans = 0
for r in range(101):
    for c in range(101):
        if board[r][c]:
            if find_square(r, c):
                ans += 1
print(ans)