def solution(n, times):
    # 최소 시간
    start = 1
    # 최대 시간
    end = 1000000000**2
    
    # 이분 탐색
    while start <= end:
        # 시간 탐색
        mid = (start + end) // 2
        
        # 심사 가능 인원 저장
        cnt = 0
        # 심사 가능 인원 탐색
        for t in times:
            # 해당 심사대에서 가능한 심사 인원
            cnt += (mid // t)
        # 심사 인원이 n보다 크거나 같으면
        if cnt >= n:
            # 시간 저장
            answer = mid
            end = mid -1
        else:
            start = mid + 1
    # 최소 시간 반환   
    return answer