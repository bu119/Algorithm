# 출입구, 쉼터, 혹은 산봉우리
# 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity라 한다.
# 다시 원래의 출입구로 돌아오는
# 등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 합니다.
# 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity
# intensity가 최소가 되도록 등산코스

# i번 지점과 j번 지점을 연결하는 등산로
# w는 두 지점 사이를 이동하는 데 걸리는 시간
# gates의 원소는 해당 지점이 출입구
# summits의 원소는 해당 지점이 산봉우리
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