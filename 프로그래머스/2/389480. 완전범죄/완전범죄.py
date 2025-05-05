def solution(info, n, m):
    
    def dfs(idx, a, b):
        nonlocal answer
        # 누적 개수가 초과하거나, 누적 값이 계산된 최솟값 이상이면 탐색 중단
        if a >= n or b >= m or answer <= a:
            return
        # 이미 방문한 상태라면 탐색 중단
        if (idx, a, b) in visited:
            return
        # 방문 체크
        visited.add((idx, a, b))
        # 마지막 물건을 품치면 최소값 갱신
        if idx == len(info):
            answer = min(answer, a)
            return
    
        dfs(idx+1, a+info[idx][0], b)
        dfs(idx+1, a, b+info[idx][1])
        

    answer = 121
    visited = set()
    dfs(0, 0, 0)
    
    if answer == 121:
        answer = -1
        
    return answer