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


t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    parent = list(range(n+1))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    ans = 'NO'
    connection = {p, q}
    for cost, c1, c2 in edges:
        if find(c1) != find(c2):
            union(c1, c2)
            if c1 in connection and c2 in connection:
                ans = 'YES'
    print(ans)
