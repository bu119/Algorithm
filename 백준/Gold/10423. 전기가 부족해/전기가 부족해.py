import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a in power_station:
        parent[b] = a
    elif b in power_station:
        parent[a] = b
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
power_station = list(map(int, input().split()))
parent = list(range(n+1))
ans = 0
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    if u in power_station and v in power_station:
        continue
    edges.append((w, u, v))
edges.sort()

for cost, u, v in edges:
    pu = find(u)
    pv = find(v)
    if pu in power_station and pv in power_station:
        continue
    if pu != pv:
        union(u, v)
        ans += cost

    if len(set(parent[1:])) == len(power_station):
        break
print(ans)