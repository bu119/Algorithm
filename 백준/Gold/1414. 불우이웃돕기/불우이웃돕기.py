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
parent = list(range(n))
maxV = 0
minV = 0
cable_cnt = 0
edges = []
for i in range(n):
    row = input()
    for j in range(n):
        if row[j] == '0':
            continue
        elif row[j] == row[j].lower():
            cable = ord(row[j]) - 96
        else:
            cable = ord(row[j]) - 38
        maxV += cable
        edges.append((cable, i, j))
edges.sort()

for cost, c1, c2 in edges:
    if find(c1) != find(c2):
        union(c1, c2)
        minV += cost
        cable_cnt += 1

if cable_cnt == n-1:
    print(maxV-minV)
else:
    print(-1)