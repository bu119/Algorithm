import heapq

def dijkstra(maxPrice):
    # 각 정점이 가질 수 있는 최소 비용 마다 총 누적 비용을 체크
    visited = [[float('inf')] * (maxPrice + 1) for _ in range(n + 1)]
    # 전체 비용, 지나온 최저 비용, 현재 위치
    heap = [(0, price[1], 1)]
    # [위치][현재최소비용]
    visited[1][price[1]] = 0

    while heap:
        # 전체 비용, 지나온 최저 비용, 현재 위치
        total_cost, min_cost, posi = heapq.heappop(heap)

        if posi == n:
            return total_cost

        if visited[posi][min_cost] < total_cost:
            continue

        for next_posi, next_dist in graph[posi]:
            new_cost = total_cost + (next_dist * min_cost)
            # 다음 도시로 갈 새로운 총 비용이 저장된 비용보다 작다면 갱신
            if new_cost < visited[next_posi][min_cost]:
                visited[next_posi][min_cost] = new_cost
                # 최소 비용 갱신
                new_min_cost = min(min_cost, price[next_posi])
                heapq.heappush(heap, (new_cost, new_min_cost, next_posi))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
price = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

print(dijkstra(max(price)))