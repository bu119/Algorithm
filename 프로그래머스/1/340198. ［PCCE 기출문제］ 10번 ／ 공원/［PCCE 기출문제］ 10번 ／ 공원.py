def solution(mats, park):
    # 공원 전체에 해당 사이즈 돗자리 자리가 있는 지 확인
    def can_place_mat(mat_size):
        for i in range(n - mat_size + 1):
            for j in range(m - mat_size + 1):
                # 돗자리 들어가면 True 반환, 안들어가면 다른 자리 탐색
                if park[i][j] == "-1" and can_fit_mat(i, j, mat_size):
                    return True
        return False

    # (x,y)를 시작으로 돗자리가 자리가 있는지 확인 
    def can_fit_mat(x, y, size):
        for dx in range(size):
            for dy in range(size):
                # 돗자리 안되면 False 반환
                if park[x+dx][y+dy] != "-1":
                    return False
        return True
                        
    
    n = len(park)
    m = len(park[0])
    # 돗자리 내림차순 정렬    
    for mat in sorted(mats, reverse=True):
        if can_place_mat(mat):
            return mat
        
    return -1