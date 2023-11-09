from collections import deque

# 1. 반시계로 4방향을 탐색해서 청소 안된 칸이 존재하면 그 칸으로 이동해서 탐색
# 2. 존재 안하면 한칸 후진 후 벽이면 작동 중지,
# 3. 벽이 아니면 1, 2 번 반복 탐색

# 4칸 중 청소 안된 칸이 있는지 반시계 방향으로 탐색
# 청소 가능한 칸으로 이동 / 후진 칸으로 이동
def check_clean(i, j, dir):
    # 현재 칸의 주변
    # 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    # 반시계 방향으로 90도 회전한 방향을 먼저 탐색 한다.
    for k in range(1, 5):
        # 현재 방향에서 반시계로 탐색
        nd = (dir - k) % 4
        ni = i + di[nd]
        nj = j + dj[nd]
        if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0:
            # 청소 간능한 칸으로 이동
            return ni, nj, nd
    # 후진
    return i - di[dir], j - dj[dir], dir

def bfs(x, y, start_d):
    deq = deque()
    # 로봇 위치, 방향
    deq.append((x, y, start_d))
    # 청소한 칸이면 2로 변경 (방문 체크)
    graph[x][y] = 2
    # 청소 횟수
    cnt = 1

    while deq:
        x, y, curr_d = deq.popleft()

        # 4칸 중 청소 안된 칸이 있는지 반시계 방향으로 탐색
        # 청소 가능한 칸으로 이동 / 후진 칸으로 이동
        nx, ny, next_d = check_clean(x, y, curr_d)

        # 후진한 위치가 벽이면 작동 멈춤
        if graph[nx][ny] == 1:
            return cnt

        # 청소 가능한 칸을 이동 했으면 청소
        if graph[nx][ny] == 0:
            # 청소 (방문 체크)
            graph[nx][ny] = 2
            # 청소 횟수 증가
            cnt += 1

        # 이동한 위치에서 다시 탐색
        deq.append((nx, ny, next_d))

    return cnt


n, m = map(int, input().split())
# 로봇 청소기 위치 (r, c), 처음 로봇 청소기 방향 d
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 북동남서(시계방향)
di = [-1,0,1,0]
dj = [0,1,0,-1]

# 0인 경우 청소되지 않은 빈 칸,
# 1인 경우 벽
print(bfs(r, c, d))