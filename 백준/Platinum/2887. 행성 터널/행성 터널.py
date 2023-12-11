import sys
input = sys.stdin.readline

# 보모 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 연결하기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
planets = []
for idx in range(n):
    x, y, z = map(int, input().split())
    planets.append((idx, x, y, z))

parent = list(range(n))
ans = 0

planet_x = sorted(planets, key=lambda x: x[1])
planet_y = sorted(planets, key=lambda x: x[2])
planet_z = sorted(planets, key=lambda x: x[3])


edges = []
for i in range(n - 1):
    edges.append((abs(planet_x[i + 1][1] - planet_x[i][1]), planet_x[i][0], planet_x[i + 1][0]))
    edges.append((abs(planet_y[i + 1][2] - planet_y[i][2]), planet_y[i][0], planet_y[i + 1][0]))
    edges.append((abs(planet_z[i + 1][3] - planet_z[i][3]), planet_z[i][0], planet_z[i + 1][0]))
edges.sort()

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost
print(ans)