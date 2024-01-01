import sys
input = sys.stdin.readline

# 1.모든 마을을 연결하는 최소 비용
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
def bfs(v):
    visited = [0] * n
    visited[v] = 1
    stack = [(v, 0)]
    worst = 0
    while stack:
        v, move_cost = stack.pop()

        if worst < move_cost:
            worst = move_cost

        for next, w in graph[v]:
            if not visited[next]:
                visited[next] = 1
                stack.append((next, move_cost + w))
    return worst


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
# 2. 두 마을을 이동하는 최고 비용 저장
worst_cost = 0
for i in range(n):
    worst_cost = max(bfs(i), worst_cost)

print(best_cost)
print(worst_cost)