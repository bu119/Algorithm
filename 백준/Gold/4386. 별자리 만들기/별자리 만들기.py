from itertools import combinations

# 부모노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = list(range(n+1))
ans = 0
stars = [list(map(float, input().split())) for _ in range(n)]
edge = []
# 별을 2개씩 뽑아 거리 계산
for s1, s2 in combinations(range(n), 2):
    x1, y1 = stars[s1]
    x2, y2 = stars[s2]
    # 두 별 사이의 거리 구하기 (소수 둘째 자리 까지)
    dist = round(((x1 - x2)**2 + (y1 - y2)**2)**(1/2), 2)
    # 두 별 사이의 거리, 별1 위치, 별2 위치
    edge.append((dist, s1, s2))
# 거리 순으로 정렬
edge.sort()

for cost, s1, s2 in edge:
    if find(s1) != find(s2):
        union(s1, s2)
        ans += cost

print(ans)