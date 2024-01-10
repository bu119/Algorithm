import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    visited = [4950001] * (n+1)
    visited[x] = 0
    heap = [(0, x)]
    while heap:
        currD, x = heapq.heappop(heap)

        if visited[x] < currD:
            continue

        for next, nextD in graph[x]:
            totalD = currD + nextD
            if totalD < visited[next]:
                visited[next] = totalD
                heapq.heappush(heap, (totalD, next))
    return visited


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    k = int(input())
    rooms = list(map(int, input().split()))
    totalDist = [0]*(n+1)
    for room in rooms:
        dist = dijkstra(room)
        for i in range(1, n+1):
            totalDist[i] += dist[i]
    ans = 0
    minV = 4950001
    for j in range(1, n+1):
        if totalDist[j] < minV:
            minV = totalDist[j]
            ans = j
    print(ans)