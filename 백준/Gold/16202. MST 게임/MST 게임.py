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


n, m, k = map(int, input().split())
edges = []
for i in range(m):
    x, y = map(int, input().split())
    edges.append((i+1, x, y))
# 각 턴의 결과를 저장
result = []
while k != 0:
    parent = list(range(n+1))
    curr_result = 0
    cnt = 0
    for cost, n1, n2 in edges:
        if find(n1) != find(n2):
            union(n1, n2)
            curr_result += cost
            cnt += 1
    if cnt == n-1:
        result.append(curr_result)
    else:
        result += [0]*k
        break
    k -= 1
    edges.pop(0)

print(' '.join(map(str, result)))