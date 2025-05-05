import heapq

def solution(info, n, m):
    
    def bfs():
        # a, b 누적 값, 몇번 째 훔치는 지
        heap = [(0, 0, 0)]
        visited = set()
        while heap:
            a, b, idx = heapq.heappop(heap)
            # 누적 개수가 조건을 초과하면 탐색 중단
            if a >= n or b >= m:
                continue
            # 이미 방문한 상태라면 탐색 중단
            if (idx, a, b) in visited:
                continue
            visited.add((idx, a, b))
            # 마지막 물건을 훔치면 최솟값 반환
            if idx == stolen_cnt:
                return a
            
            heapq.heappush(heap, (a+info[idx][0], b, idx+1))
            heapq.heappush(heap, (a, b+info[idx][1], idx+1))
        
        return -1
    
    
    stolen_cnt = len(info)
    answer = bfs()
    return answer