import sys, heapq
input = sys.stdin.readline

def dijkstra(x):
    visited = [maxV]*(n+1)
    savePath = [0]*(n+1)
    visited[x] = 0
    heap = [(0, x)]
    while heap:
        currT, x = heapq.heappop(heap)

        if visited[x] < currT:
            continue

        for next, nextT in graph[x]:
            totalT = currT + nextT
            if totalT < visited[next]:
                visited[next] = totalT
                savePath[next] = x
                heapq.heappush(heap, (totalT, next))
    return savePath


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

maxV = 10*m+1
savePaths = dijkstra(1)
ans = set()
for i in range(2, n+1):
    j = savePaths[i]
    if j != 0 and (i, j) not in ans and (j, i) not in ans:
        ans.add((i, j))
        
print(len(ans))
for a, b in ans:
    print(a, b)