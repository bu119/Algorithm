import heapq

def solution(n, paths, gates, summits):

    def dijkstra():
        visited = [10000001]*(n+1)
        heap = []
        # 각 출발점에서 산봉우리 가는 길 탐색
        for gate in gates:
            heap.append((0, gate))
            visited[gate] = 0
        
        while heap:
            dist, now = heapq.heappop(heap)
            # 저장된 거리가 더 작거나 산봉우리를 만나면 탐색 안함
            if visited[now] < dist or now in set_summits:
                continue
            
            for next_dist, next in graph[now]:
                # 출발점을 만나면 탐색 안함
                if next in set_gates:
                    continue
                max_dist = max(dist, next_dist)
                # intensity(가장 긴 시간) 작으면 값 갱신
                if max_dist < visited[next]:
                    visited[next] = max_dist
                    heapq.heappush(heap, (max_dist, next))
        
        return visited

    
    # 등산로 양방향 그래프로 저장
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    set_summits = set(summits)
    set_gates = set(gates)
    
    answer = [0, 10000001]
    summits.sort()
    # 각 산봉우리까지 intensity 찾기
    intensity = dijkstra()
    # 최소 intensity 찾기
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer[0] = summit
            answer[1] = intensity[summit]

    return answer