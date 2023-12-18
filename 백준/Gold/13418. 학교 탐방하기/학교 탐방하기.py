import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
# 최선 경로 부모 저장
min_parent = list(range(n+1))
# 최악 경로 부모 저장
max_parent = list(range(n+1))
edges = []
best = 0
worst = 0
for _ in range(m+1):
    a, b, c = map(int, input().split())
    # 오르막길에 가중치를 더 준다. (내리막길부터 연결하기 위해)
    # 오르막길이면 가중치를 1로 준다.
    if c == 0:
        edges.append((1, a, b))
    else:
        edges.append((0, a, b))
edges.sort()
for i in range(m+1):
    # 최선
    min_cost, b1, b2 = edges[i]
    # 최악
    max_cost, s1, s2 = edges[m-i]

    # 최선 경로
    if find(min_parent, b1) != find(min_parent, b2):
        union(min_parent, b1, b2)
        best += min_cost
    # 최악 경로
    if find(max_parent, s1) != find(max_parent, s2):
        union(max_parent, s1, s2)
        worst += max_cost
print(worst**2 - best**2)