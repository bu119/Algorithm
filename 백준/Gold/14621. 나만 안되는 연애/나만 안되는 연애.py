import sys
input = sys.stdin.readline

# 부모 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 연결하기
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
univ = input().split()
parent = list(range(n+1))
# 모든 학교 연결 여부 체크
visited = set()
ans = 0
edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    # 다른 성별 대학교 길만 저장
    if univ[u-1] != univ[v-1]:
        edges.append((d, u, v))
        # 학교 방문 체크
        visited.add(u)
        visited.add(v)

# 모든 학교 연결 여부
# 불가
if len(visited) != n:
    ans = -1
# 가능
else:
    # 거리순으로 정렬
    edges.sort()
    # 최단 거리 계산
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            ans += cost
print(ans)