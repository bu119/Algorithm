import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    dist = [50000001] * (n+1)
    heap = [(0, x)]
    dist[x] = 0
    while heap:
        currCow, x = heapq.heappop(heap)

        if dist[x] < currCow:
            continue

        for next, nextCow in graph[x]:
            totalCow = currCow + nextCow
            if totalCow < dist[next]:
                dist[next] = totalCow
                heapq.heappush(heap, (totalCow, next))
    return dist[n]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
print(dijkstra(1))