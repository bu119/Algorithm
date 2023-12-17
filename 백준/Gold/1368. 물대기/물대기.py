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
parent = list(range(n+1))
# 최소 비용 저장
ans = 0
edges = []
# 우물을 파는 비용은 0번 노드와 연결되는 것으로 한다. (우물을 최소 1개는 파야한다.)
for k in range(n):
    w = int(input())
    edges.append((w, 0, k+1))
# 논들 사이에 물을 끌어오는 비용 저장
for i in range(n):
    pi = list(map(int, input().split()))
    for j in range(n):
        edges.append((pi[j], i+1, j+1))
# 금액 별로 정렬
edges.sort()
for cost, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        ans += cost
print(ans)