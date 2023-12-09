import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    # 부모 노드 찾기
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 집의 개수 N, 길의 개수 M
n, m = map(int, input().split())
parent = list(range(n+1))
edge = []
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
    
edge.sort()

for cost, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        ans += cost
        last_cost = cost
        
print(ans - last_cost)