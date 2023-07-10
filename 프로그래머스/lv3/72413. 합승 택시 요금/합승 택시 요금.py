import heapq

def dijkstra(start, end, n):
    global road_graph, maxV
    charge = [maxV] * (n + 1)

    heap = [(0, start)]
    charge[start] = 0

    while heap:
        cost, now = heapq.heappop(heap)
        
        # 요금배열에 저장된 값 보다 적은 값의 요금이 등장하면 이후 거리도 갱신 
        if charge[now] < cost:
            continue

        for e, price in road_graph[now]:
            new_cost = cost + price
             # 기존 거리 비용이랑 새로운 거리 비용을 더한 값이 저장된 요금보다 작을 때 값을 갱신
            if new_cost < charge[e]:
                charge[e] = new_cost
                heapq.heappush(heap, (new_cost, e))

    return charge[end]


def solution(n, s, a, b, fares):
    global road_graph, maxV

    road_graph = [[] for _ in range(n+1)]
    maxV = 0

    for c, d, f in fares:
        road_graph[c].append((d, f))
        road_graph[d].append((c, f))
        maxV += f

    # 각자 바로 가는 경우
    answer = dijkstra(s, a, n) + dijkstra(s, b, n)

    # 합승했다가 찢어지는 경우 (모든 경우 계산)
    for i in range(1, n + 1):

        # 시작점 제외
        if i == s:
            continue

        answer = min(answer, (dijkstra(s, i, n) + dijkstra(i, a, n) + dijkstra(i, b, n)))

    return answer
