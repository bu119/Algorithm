import sys
sys.setrecursionlimit(10**9)
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


n, m = map(int, input().split())
s, e = map(int, input().split())
parent = list(range(n+1))
edges = []
for _ in range(m):
    h1, h2, k = map(int, input().split())
    edges.append((k, h1, h2))
edges.sort(reverse=True)
ans = 0
for cost, i1, i2 in edges:
    if find(i1) != find(i2):
        union(i1, i2)
        # s에서 e로 가는 간선이 생기면 부모가 같아진다.
        # 내림차순 정렬이므로 현재 연결 비용이 가장 작은 값이다.
        if find(s) == find(e):
            ans = cost
            break
print(ans)