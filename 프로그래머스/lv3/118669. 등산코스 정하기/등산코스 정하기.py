# 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity라고 부른다.
# intensity가 최소가 되도록 등산코스를 정하려고 한다.
# intensity가 최소가 되는 등산코스가 여러 개라면 그중 산봉우리의 번호가 가장 낮은 등산코스를 선택한다.

import heapq


def dijkstra(n, gates):
    global time_graph, check_summits, answer
    
    min_summit = 50000
    min_intensity = 10000001
    
    # 각 코스의 최소 intensity 저장
    visited = [10000001] * (n+1)
    heap = []
    
    # 출입구 값 넣기
    for gate in gates:
        heapq.heappush(heap, (0, gate))
        visited[gate] = 0
    
    while heap:
        
        intensity, now = heapq.heappop(heap)
        
        # intensity가 저장된 값보다 크면 굳이 갈 필요없음
        # 이 문제에서는 intensity의 최소가 되는 등산코스 구해야함
        if visited[now] < intensity:
            continue
        
        # 봉우리 나오면 봉우리와 현재까지 최소 intensity 값 저장
        if now in check_summits:
            # min_intensity는 갱신되는 최솟값
            if visited[now] < min_intensity:
                min_summit = now
                min_intensity = visited[now]
            elif visited[now] == min_intensity:
                min_summit = min(now, min_summit)
            
            continue
        
        for posi, inte in time_graph[now]:
            # 현재 경로의 최대 intensity 구하기
            # intensity는 휴식 없이 이동해야 하는 시간 중 가장 긴 시간
            new_inte = max(inte, intensity)
            
            # 현재 경로의 최대값이 다른 경로 값보다 작으면 갱신
            if new_inte < visited[posi]:
                visited[posi] = new_inte
                heapq.heappush(heap, (new_inte, posi))
    
    return [min_summit, min_intensity]


def solution(n, paths, gates, summits):
    global time_graph, check_summits
    
    # [산봉우리의 번호, intensity의 최솟값]
    
    time_graph = [[] for _ in range(n+1)]
    check_summits = set(summits)
    
    for i, j, w in paths:
        time_graph[i].append((j,w))
        time_graph[j].append((i,w))

    answer = dijkstra(n, gates)

    return answer