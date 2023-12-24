from collections import deque

# 거리 저장
def bfs(sx, sy):
    global edges
    k_cnt = 0
    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0
    deq = deque()
    deq.append((sx, sy))
    while deq:
        x, y = deq.popleft()

        if graph[x][y] == 'K' or graph[x][y] == 'S':
            k_cnt += 1
            edges.append((visited[x][y], key_p[(sx, sy)], key_p[(x, y)]))

        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1 and graph[ni][nj] != '1':
                visited[ni][nj] = visited[x][y] + 1
                deq.append((ni, nj))

    return k_cnt

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
graph = []
si, sj = 0, 0
# 열쇠 위치 저장 {위치: 인덱스}
key_p = dict()
idx = 0
for i in range(n):
    row = input()
    graph.append(row)
    for j in range(n):
        if row[j] == 'S' or row[j] == 'K':
            key_p[(i, j)] = idx
            idx += 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
parent = list(range(m+1))
edges = []
flag = 1
for r, c in key_p.keys():
    key_cnt = bfs(r, c)
    if key_cnt != m+1:
        flag = 0
        print(-1)
        break
if flag:
    edges.sort()
    ans = 0
    for cost, k1, k2 in edges:
        if find(k1) != find(k2):
            union(k1, k2)
            ans += cost
    print(ans)