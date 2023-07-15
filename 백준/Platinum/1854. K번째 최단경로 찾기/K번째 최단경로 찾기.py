import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [[INF] * k for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra():
    heap = []
    visited[1][0] = 0
    heapq.heappush(heap, (0, 1))

    while heap:
        now_time, city = heapq.heappop(heap)

        if visited[city][k - 1] < now_time:
            continue

        for node, new in graph[city]:
            cost = now_time + new
            if cost < visited[node][k - 1]:
                visited[node][k-1] = cost
                visited[node].sort()
                heapq.heappush(heap, (cost, node))


dijkstra()

for i in range(1, n + 1):
    if visited[i][k - 1] == INF:
        print(-1)
    else:
        print(visited[i][k - 1])