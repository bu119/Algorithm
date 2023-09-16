def solution(n, times):
    start = 1
    end = 1000000000**2
    
    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2
        
        # 심사 가능 인원 저장
        cnt = 0
        # 심사 가능 인원 탐색
        for t in times:
            cnt += (mid // t)
        
        if cnt >= n:
            answer = mid
            end = mid -1
        else:
            start = mid + 1
            
    return answer