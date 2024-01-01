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


n, m = map(int, input().split())
parent = list(range(n+1))
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
escape_time = list(map(int, input().split()))
# 출구는 0
for i in range(n):
    edges.append((escape_time[i], 0, i+1))
edges.sort()
ans = 0
for cost, r1, r2 in edges:
    if find(r1) != find(r2):
        union(r1, r2)
        ans += cost
print(ans)