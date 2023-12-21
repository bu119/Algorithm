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


n, m, t = map(int, input().split())
parent = list(range(n+1))
ans = 0
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
conquest = 0
for cost, c1, c2 in edges:
    if find(c1) != find(c2):
        union(c1, c2)
        ans += cost + (conquest * t)
        conquest += 1
print(ans)