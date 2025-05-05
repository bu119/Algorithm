def solution(info, n, m):
    
    def dfs(idx, a, b):
        nonlocal answer
        # 누적 개수가 조건을 초과하거나, 현재 누적 값이 이미 계산된 최솟값보다 같거나 크면 해당 탐색 종료
        if a >= n or b >= m or answer <= a:
            return
        # 이미 방문한 상태라면 중단
        if (idx, a, b) in visited:
            return
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