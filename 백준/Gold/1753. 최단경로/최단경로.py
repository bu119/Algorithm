import sys, heapq
input = sys.stdin.readline

def dijkstra(k):

    heap = [(0, k)]
    visited[k] = 0

    while heap:

        dist, now = heapq.heappop(heap)

        if visited[now] < dist:
            continue

        for node, d in graph[now]:
            new_dist = dist + d
            if new_dist < visited[node]:
                visited[node] = new_dist
                heapq.heappush(heap, (new_dist, node))


V, E = map(int,input().split())
k = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

visited = [3000000] * (V + 1)

dijkstra(k)

for i in range(1, V+1):
    if visited[i] == 3000000:
        print('INF')
    else:
        print(visited[i])