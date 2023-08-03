from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for node in sorted(graph[v]):
        if not visited[node]:
            dfs(node)

def bfs(v):
    deq = deque()
    deq.append(v)
    visited[v] = 1

    while deq:
        v = deq.popleft()

        print(v, end=' ')

        for node in sorted(graph[v]):
            if not visited[node]:
                visited[node] = 1
                deq.append(node)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
dfs(v)
print()
visited = [0]*(n+1)
bfs(v)