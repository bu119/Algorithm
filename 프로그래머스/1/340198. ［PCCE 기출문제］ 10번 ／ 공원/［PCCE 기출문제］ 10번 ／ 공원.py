def solution(mats, park):
    # 해당 사이즈 돗자리 깔수 있는 지 확인하는 함수
    def check_mat_space(x, y, size):
        for dx in range(size):
            for dy in range(size):
                nx = x + dx
                ny = y + dy
                if not(0 <= nx < n and 0 <= ny < m) or park[nx][ny] != "-1":
                    return False
        return True


    n = len(park)
    m = len(park[0])
    # 돗자리 내림차순 정렬
    mats.sort(reverse=True)
    
    # 가능한 돗자리 최대 크기 저장 
    answer = -1
    # 가능한 최대 크기 돗자리 인덱스 저장
    idx = len(mats) - 1
    
    # 공원 순회
    for i in range(n):
        for j in range(m):
            # 빈 자리 나오면 어떤 크기의 돗자리 가능한지 확인
            if park[i][j] == "-1":
                # 돗자리 크기 내림 차순으로 확인
                for k in range(idx+1):
                    # x 크기 돗자리 가능하면 갱신
                    if check_mat_space(i, j, mats[k]):
                        # 가장 큰 돗자리면 돗자리 크기 바로 반환
                        if k == 0:
                            return mats[k]
                        # 인덱스 갱신 (다음 탐색은 더 큰 사이즈만 함)
                        idx = min(idx, k-1)
                        # 돗자리 크기 갱신
                        answer = max(answer, mats[k]) 
    return answer