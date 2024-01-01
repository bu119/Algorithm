import sys
input = sys.stdin.readline

# 1.모든 마을을 연결하는 최소 비용 구하기
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

# 2.두 마을을 이동하는 최고 비용 구하기
def dfs(v, road_cost):
    global worst_cost
    if worst_cost < road_cost:
        worst_cost = road_cost

    for next, w in graph[v]:
        if not visited[next]:
            visited[next] = 1
            dfs(next, road_cost + w)


# 교역로는 양 방향으로 이동
# 1.모든 마을과 마을을 연결하는 최소 비용
# 2.두 마을을 이동하는 최단 경로의 최고 비용
n, k = map(int, input().split())
parent = list(range(n))
edges = []
# 선택된 길 저장
graph = [[] for _ in range(n)]
for _ in range(k):
    # 두 마을을 연결하는 비용 c
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
# 모든 마을을 연결하는 최소 비용 저장
best_cost = 0
for cost, c1, c2 in edges:
    if find(c1) != find(c2):
        union(c1, c2)
        best_cost += cost
        # 이동 가능한 마을과 비용 정보 저장
        graph[c1].append((c2, cost))
        graph[c2].append((c1, cost))
# 두 마을을 이동하는 최고 비용 저장
worst_cost = 0
for i in range(n):
    # 끝에서 이동해야 거리가 길다.
    if len(graph[i]) == 1:
        visited = [0] * n
        visited[i] = 1
        dfs(i, 0)
print(best_cost)
print(worst_cost)