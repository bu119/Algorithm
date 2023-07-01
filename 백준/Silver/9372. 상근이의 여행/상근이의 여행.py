import sys
from collections import deque # deque를 통해 시간복잡도를 줄였다.

input = sys.stdin.readline

def bfs(node):
    # 들려야 할 정점 저장
    que = deque()
    que.append(node)

    # 현재 노드 방문 처리
    visited[node] = 1
    cnt = 0

    while que:

        if visited.count(1) == n:
            return cnt

        x = que.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                que.append(i)
                cnt += 1


t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0]*(n+1)
    print(bfs(1))