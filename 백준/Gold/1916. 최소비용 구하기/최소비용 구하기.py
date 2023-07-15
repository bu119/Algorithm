import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v, u, w = map(int, input().split())
    graph[v].append((u, w))

s, e = map(int, input().split())

def dijkstra(s,e):
    visited = [100000000]*(n+1)

    heap = [(0,s)]
    visited[s] = 0

    while heap:

        cost, now = heapq.heappop(heap)

        if now == e:
            return cost

        if visited[now] < cost:
            continue

        for node, price in graph[now]:
            new_cost = cost + price
            if new_cost < visited[node]:
                visited[node] = new_cost
                heapq.heappush(heap,(new_cost, node))


print(dijkstra(s,e))