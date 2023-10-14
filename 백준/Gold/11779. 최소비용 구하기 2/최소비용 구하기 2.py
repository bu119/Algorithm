import sys, heapq
input = sys.stdin.readline

def dijkstra(start, end):
    global route
    # 비용 저장
    visited = [10000000001] * (n + 1)
    # 비용, 현재 위치
    heap = [(0, start)]
    # 최소 비용 저장
    visited[start] = 0

    while heap:
        curCost, curCity = heapq.heappop(heap)

        # 저장된 비용보다 크면 탐색 안함
        if visited[curCity] < curCost:
            continue

        for nextCity, moveCost in graph[curCity]:
            totalCost = curCost + moveCost
            # 비용이 적으면 갱신
            if totalCost < visited[nextCity]:
                # 최소 비용 저장
                visited[nextCity] = totalCost
                # 경로 갱신 (이전 도시 저장)
                route[nextCity] = curCity

                heapq.heappush(heap, (totalCost, nextCity))

    return visited[end]


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())
# 도시 이동 경로 저장
route = [0] * (n+1)

# 출력
print(dijkstra(start, end))

# 도시 이동 경로
preCity = end
cityRoute = [str(end)]
# 출발점은 0이 나온다.
while route[preCity]:
    preCity = route[preCity]
    cityRoute.append(str(preCity))
    
# 출력
print(len(cityRoute))
print(' '.join(reversed(cityRoute)))