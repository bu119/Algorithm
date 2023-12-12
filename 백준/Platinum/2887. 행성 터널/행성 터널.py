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
edges = []
for i in range(1, 4):
    # x, y, z 각 위치 마다 오름차순 정렬
    planet = sorted(planets, key=lambda x: x[i])
    # 이웃한 숫자의 차이 저장
    for j in range(n-1):
        edges.append((planet[j + 1][i] - planet[j][i], planet[j][0], planet[j + 1][0]))
edges.sort()

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost
print(ans)