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
# 모든 건물을 연결하는 도로 비용
maxV = 0
# 최소 도로 비용
minV = 0
# 최소 연결 도로 개수
road_cnt = 0

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    maxV += c
    edges.append((c, a, b))
edges.sort()

for cost, b1, b2 in edges:
    if find(b1) != find(b2):
        union(b1, b2)
        minV += cost
        road_cnt += 1
        
if road_cnt == n-1:
    print(maxV-minV)
else:
    print(-1)