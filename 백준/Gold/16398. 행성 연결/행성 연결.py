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


n = int(input())
parent = list(range(n))
ans = 0
edges = []
for i in range(n):
    planets = list(map(int, input().split()))
    for j in range(n):
        if i <= j:
            continue
        edges.append((planets[j], i, j))
edges.sort()

for cost, p1, p2 in edges:
    if find(p1) != find(p2):
        union(p1, p2)
        ans += cost
print(ans)