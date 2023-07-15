import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))


def dijkstra():
    heap = [(0,1)]
    visited[1].append(0)

    while heap:

        now_time, city = heapq.heappop(heap)

        for node, new in graph[city]:
            new_time = now_time + new

            if not visited[node] or len(visited[node]) < k:
                heapq.heappush(visited[node], -new_time)
                heapq.heappush(heap, (new_time, node))

            elif new_time < -visited[node][0]:
                heapq.heappop(visited[node])
                heapq.heappush(visited[node], -new_time)
                heapq.heappush(heap, (new_time, node))


dijkstra()

for j in range(1,n+1):
    if len(visited[j]) < k:
        print(-1)
    else:
        print(-visited[j][0])
