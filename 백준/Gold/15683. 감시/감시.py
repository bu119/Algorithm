# CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다.
# 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다.
# CCTV가 감시할 수 없는 영역은 사각지대라고 한다.
# CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향
from copy import deepcopy


# 각 카메라 감시 구역
def camera1(curr_visited, x, y, dir):
    while 0 <= x < n and 0 <= y < m and graph[x][y] != 6:
        curr_visited[x][y] = 1
        x += di[dir]
        y += dj[dir]
    return curr_visited


def camera2(curr_visited, x, y, dir):
    case = {0: (0, 2), 1: (1, 3)}

    for d in case[dir]:
        nx = x
        ny = y
        while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 6:
            curr_visited[nx][ny] = 1
            nx += di[d]
            ny += dj[d]

    return curr_visited


def camera3(curr_visited, x, y, dir):
    case = {0: (3, 0), 1: (0, 1), 2: (1, 2), 3: (2, 3)}

    for d in case[dir]:
        nx = x
        ny = y
        while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 6:
            curr_visited[nx][ny] = 1
            nx += di[d]
            ny += dj[d]

    return curr_visited


def camera4(curr_visited, x, y, dir):
    case = {0: (2, 3, 0), 1: (3, 0, 1), 2: (0, 1, 2), 3: (1, 2, 3)}

    for d in case[dir]:
        nx = x
        ny = y
        while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 6:
            curr_visited[nx][ny] = 1
            nx += di[d]
            ny += dj[d]

    return curr_visited


def camera5(curr_visited, x, y):

    for d in range(4):
        nx = x
        ny = y
        while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 6:
            curr_visited[nx][ny] = 1
            nx += di[d]
            ny += dj[d]
    return curr_visited

# CCTV 사각지대 개수 체크
def blind_spot(last_visited):
    global minV

    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0 and last_visited[x][y] == 0:
                cnt += 1

    minV = min(minV, cnt)

# CCTV 감시 가능 구역 체크
def dfs(idx, curr_visited):

    if idx == cctv_cnt:
        blind_spot(curr_visited)
        return

    x, y, num = cctv[idx]
    if num == 1:
        for k in range(4):
            next_visited = camera1(deepcopy(curr_visited), x, y, k)
            dfs(idx + 1, next_visited)
    elif num == 2:
        for k in range(2):
            next_visited = camera2(deepcopy(curr_visited), x, y, k)
            dfs(idx + 1, next_visited)
    elif num == 3:
        for k in range(4):
            next_visited = camera3(deepcopy(curr_visited), x, y, k)
            dfs(idx + 1, next_visited)
    elif num == 4:
        for k in range(4):
            next_visited = camera4(deepcopy(curr_visited), x, y, k)
            dfs(idx + 1, next_visited)
    else:
        next_visited = camera5(deepcopy(curr_visited), x, y)
        dfs(idx + 1, next_visited)


n, m = map(int, input().split())
# CCTV 위치 저장
cctv = []
# CCTV 개수
cctv_cnt = 0
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(m):
        if 0 < row[j] < 6:
            cctv.append((i, j, row[j]))
            cctv_cnt += 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
visited = [[0]*m for _ in range(n)]

minV = 65
dfs(0, visited)
print(minV)