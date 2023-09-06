import sys
input = sys.stdin.readline

# 각 세대의 이동 방향과 마지막 위치를 저장 함수
def dragon_curve():
    global last_i, last_j, move
    # 이전 세대의 끝점을 다음 세대의 시작점으로 갱신

    # 끝 점을 기준으로 90도 시계 방향 회전시킨 선분의 방향을 순서대로 추가한다.
    m = len(move)
    for k in range(m-1, -1, -1):
        # k값 0, 1, 2, 3으로 나오게 변경
        z = (move[k] + 1) % 4
        # 변경된 위치값
        ni = last_i + di[z]
        nj = last_j + dj[z]
        if 0 <= ni <= 100 and 0 <= nj <= 100:
            # 방문 체크
            graph[ni][nj] = 1
            # 이동 방향을 추가로 저장
            move.append(z)
            last_i = ni
            last_j = nj


# 정사각형이 몇개인지 찾는 함수
def find_square():
    cnt = 0
    for r in range(100):
        for c in range(100):
            # 정사각형 이면
            if graph[r][c] and graph[r + 1][c] and graph[r][c + 1] and graph[r + 1][c + 1]:
                cnt += 1
    return cnt


n = int(input())
graph = [[0] * 101 for _ in range(101)]
# 동북서남
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

# x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
for _ in range(n):
    # x축(열) = j, y축(행) = i
    j, i, d, g = map(int, input().split())
    # 시작점 방문 체크
    graph[i][j] = 1
    # 이동 방향 저장
    move = [d]
    # 0세대 이동 위치
    last_i = i + di[d]
    last_j = j + dj[d]
    # 이동 방문 체크
    graph[last_i][last_j] = 1

    # g번 반복 (1세대부터 g세대까지)
    for _ in range(g):
        # 끝 점을 기준으로 90도 시계 방향 회전 시킨 모양의 위치와 방향을 추가하는 함수
        dragon_curve()

# 정사각형의 개수 찾기
print(find_square())
