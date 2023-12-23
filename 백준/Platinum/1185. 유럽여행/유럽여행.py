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


n, p = map(int, input().split())
country_cost = [0] + [int(input()) for _ in range(n)]
parent = list(range(n+1))
# 가장 방문 비용이 적은 곳을 출발점 (한번 더 추가되므로)
ans = min(country_cost[1:])
edges = []
for _ in range(p):
    s, e, l = map(int, input().split())
    # 돌아 오니까 길은 두번씩 방문, 정점은 간선 수만큼 방문
    # 길 통과 비용 * 2 + s 방문 비용 + e 방문 비용으로 가중치에 반영해주기
    edges.append((l*2 + country_cost[s] + country_cost[e], s, e))
edges.sort()
for cost, s, e in edges:
    if find(s) != find(e):
        union(s, e)
        ans += cost
print(ans)