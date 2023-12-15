import sys
input = sys.stdin.readline

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


n, m, k = map(int, input().split())
power_station = set(map(int, input().split()))
parent = list(range(n+1))
# 도시에는 발전소가 반드시 하나만 연결되야하므로
# 발전소의 부모는 다 0으로 초기화
for i in power_station:
    parent[i] = 0

ans = 0
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    # 발전소에서 발전소로 가는 길
    if parent[u] == parent[v]:
        continue
    edges.append((w, u, v))
    
edges.sort()
# 경로의 개수 = 전체 노드 - 발전소 노드
road_cnt = n - len(power_station)

for cost, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        ans += cost
        road_cnt -= 1

print(ans)