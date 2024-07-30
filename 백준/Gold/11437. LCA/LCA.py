import sys
# 런타임 오류를 피하기
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        # 이미 깊이를 구했다면 넘기기
        if c[y]:
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록 맞춘다.
    while d[a] != d[b]:
        # 깊이가 큰 노드가 부모 노드로 이동
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 깊이는 같지만 두 노드의 부모가 서로 다를 경우
    while a != b:
        # 두 노드를 부모 노드로 이동
        a = parent[a]
        b = parent[b]
    return a


n = int(input())

# 부모 노드 정보
parent = [0] * (n + 1)
# 각 노드까지의 깊이
d = [0] * (n + 1)
# 각 노드의 깊이가 계산되었는지 여부
c = [0] * (n + 1)
# 그래프(graph) 정보
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드는 1번 노드
dfs(1, 0)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))