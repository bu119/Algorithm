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
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if i == 0 or j == 0 or i > j:
            continue
        edges.append((row[j], i+1, j+1))
edges.sort()
c_cost = 0
c_cnt = 0
c_num = []
for cost, c1, c2 in edges:
    if find(c1) != find(c2):
        union(c1, c2)
        c_cost += cost
        c_cnt += 1
        c_num.append((c1, c2))

print(c_cost, c_cnt)
for num1, num2 in c_num:
    print(num1, num2)