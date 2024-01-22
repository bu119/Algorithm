from collections import deque
import sys
input = sys.stdin.readline

def bfs(e):
    deq = deque()
    # 시작점 찾아 저장
    for i in range(1, n+1):
        if parent[i] == i:
            deq.append(i)
            visited[i] = d[i]

    while deq:
        v = deq.popleft()

        for nextV in graph[v]:
            # 진입 경로 줄이기
            linkCnt[nextV] -= 1
            visited[nextV] = max(visited[nextV], visited[v] + d[nextV])
            # 지나와야하는 건물을 다 지으면
            if linkCnt[nextV] == 0:
                deq.append(nextV)
    return visited[e]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    linkCnt = [0] * (n+1)
    parent = list(range(n + 1))
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        parent[y] = x
        # y 진입 경로 개수 저장
        linkCnt[y] += 1

    w = int(input())
    # 해당 건물까지 걸리는 시간 저장
    visited = [0] * (n + 1)
    print(bfs(w))