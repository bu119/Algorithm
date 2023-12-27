from collections import deque
import sys
sys.setrecursionlimit(10**9)
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

def bfs(s, e):
    visited = [0]*(n+1)
    visited[s] = 1
    deq = deque()
    # 정점, 최대 금빼빼로 개수 저장
    deq.append((s, 1000001))
    while deq:
        v, max_cnt = deq.popleft()

        if v == e:
            return max_cnt

        for u, w in graph[v]:
            if not visited[u]:
                visited[u] = 1
                deq.append((u, min(max_cnt, w)))
    return 0


n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
parent = list(range(n+1))
edges = []
for _ in range(m):
    h1, h2, k = map(int, input().split())
    edges.append((k, h1, h2))
edges.sort(reverse=True)
for cost, i1, i2 in edges:
    if find(i1) != find(i2):
        union(i1, i2)
        graph[i1].append((i2, cost))
        graph[i2].append((i1, cost))

print(bfs(s, e))