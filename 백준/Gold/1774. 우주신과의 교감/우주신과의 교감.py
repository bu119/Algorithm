from itertools import combinations
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
god = dict()
parent = list(range(n+1))
ans = 0
edges = []
for i in range(n):
    god[i+1] = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for g1, g2 in combinations(range(1, n+1), 2):
    x1, y1 = god[g1]
    x2, y2 = god[g2]
    edges.append((((x1-x2)**2 + (y1-y2)**2)**(1/2), g1, g2))
edges.sort()

for cost, g1, g2 in edges:
    if find(g1) != find(g2):
        union(g1, g2)
        ans += cost
print(f"{ans:.2f}")