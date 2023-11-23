# 연결된 섬 영역 확인
def bfs(x, y):
    global island

    stack = [(x, y)]
    island_visited[x][y] = 1
    island_info = {(i, j)}

    while stack:
        x, y = stack.pop()

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and island_visited[nx][ny] == 0:
                island_visited[nx][ny] = 1
                stack.append((nx, ny))
                island_info.add((nx, ny))
    return island_info


def make_bridge(x, y, d):
    bridge = set()
    while graph[x][y] == 0:
        bridge.add((x, y))
        x += di[d]
        y += dj[d]
        if not (0 <= x < n and 0 <= y < m):
            return 0, set()
    # 인접한 섬 저장
    for key in island:
        if (x, y) in island[key]:
            return key, bridge


# 각 섬에서 가능한 다리 경우의수 1개씩 뽑고
def dfs(idx):
    global select_bridge, min_bridge

    # 마지막 섬의 다리 선택이 끝나면
    if idx > island_cnt:
        # 연결 되어 있는지 체크
        cnt = 0
        # a - b - c 섬으로 이동하는 다리 생성
        for a in range(1, island_cnt + 1):
            b = select_bridge[a]
            c = select_bridge[b]
            # a == c 가 같은 길이면
            if a == c:
                cnt += len(adj_island[a][b]) / 2
            else:
                cnt += len(adj_island[a][b])

        if is_connect_bfs():
            min_bridge = min(min_bridge, cnt)
        return

    for adj in adj_island[idx]:
        # 섬 번호 저장
        select_bridge.append(adj)
        dfs(idx+1)
        select_bridge.pop()


# 한개의 섬으로 연결되어 있는 지 확인
def is_connect_bfs():
    adj_visited = [0] * (island_cnt + 1)
    adj_graph = [[] for _ in range(island_cnt+1)]

    for v in range(1, island_cnt + 1):
        adj_graph[v].append(select_bridge[v])
        adj_graph[select_bridge[v]].append(v)

    stack = [1]
    adj_visited[1] = 1

    while stack:
        v = stack.pop()

        if sum(adj_visited) == island_cnt:
            return True

        for w in adj_graph[v]:
            if adj_visited[w] == 0:
                adj_visited[w] = 1
                stack.append(w)
    return False


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 동 남 서 북
di = [0, 1, 0 ,-1]
dj = [1, 0, -1, 0]

# 섬 개수와 위치 파악
island = dict()
island_visited = [[0]*m for _ in range(n)]
# 섬 번호는 1부터
island_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and island_visited[i][j] == 0:
            island_cnt += 1
            island[island_cnt] = bfs(i, j)

# 각 섬에서 가능한 다른 섬 찾기
adj_island = dict()
for key in island:
    adj_island[key] = dict()
    for i, j in island[key]:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0:
                adj_num, bridge_posi = make_bridge(ni, nj, k)
                if len(bridge_posi) > 1:
                    if adj_island[key].get(adj_num):
                        if len(adj_island[key][adj_num]) > len(bridge_posi):
                            adj_island[key][adj_num] = bridge_posi
                    else:
                        adj_island[key][adj_num] = bridge_posi

# 이동하는 섬 위치 저장
select_bridge = [0]
# 시작 섬, 다리 너비
min_bridge = 601
dfs(1)
if 601 == min_bridge:
    min_bridge = -1
print(int(min_bridge))