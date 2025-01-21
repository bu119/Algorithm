import sys
input = sys.stdin.readline

# 기존 선을 90도 회전하는 위치 저장 함수
def move_90(li, lj):
    global move_d
    # 시작점을 마지막 지점으로 설정하고
    # 마지막 지점부터 + 1을 해서 반시계 방향으로 추가해주면 된다.
    m = len(move_d)
    for z in range(m-1, -1, -1):
        # k값 0, 1, 2, 3으로 나오게 변경
        k = (move_d[z] + 1) % 4
        # 변경된 위치값
        ni = li + di[k]
        nj = lj + dj[k]
        if 0 <= ni <= 100 and 0 <= nj <= 100:
            # 방문 체크
            board[ni][nj] = 1
            move_d.append(k)
            li = ni
            lj = nj

    return li, lj


# 정사각형인지 판별하는 함수
def find_square():
    ans = 0
    for r in range(100):
        for c in range(100):
            if board[r][c] and board[r + 1][c] and board[r][c + 1] and board[r + 1][c + 1]:
                ans += 1
    return ans


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

    # g번 반복 (1세대부터 g세대까지)
    for _ in range(g):
        # 현재 선 모양을 반시계방향으로 90도 회전하여 연결 방향을 추가해주는 함수
        # 마지막 위치를 return
        last_i, last_j = move_90(last_i, last_j)

# 정사각형의 개수 찾기
print(find_square())