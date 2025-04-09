from copy import deepcopy

def solution(key, lock):
    # 열쇠 회전
    def rotate_90(matrix):
        # 90도 회전
        return [row for row in zip(*matrix[::-1])]
    
    # 열쇠와 자물쇠가 일치하는 지 확인
    def check_match(area):
        for i in range(n):
            for j in range(n):
                if area[i + m - 1][j + m - 1] != 1:
                    return False
        return True
    
    # 열쇠를 회전 및 이동시켜 자물쇠 열 수 있는 지 확인
    def can_unlock():
        rotated_key = key
        for _ in range(4):
            # 행과 열 모두 0 ~ m+n-2 까지 이동
            for dx in range(m + n - 1):
                for dy in range(m + n - 1):
                    # 자물쇠 복사
                    lock_area = deepcopy(padded_lock)
                    # 열쇠를 자물쇠에 덮기
                    for x in range(m):
                        for y in range(m):
                            lock_area[dx + x][dy + y] += rotated_key[x][y]
                    # 열쇠와 자물쇠가 일치하는 지 확인
                    if check_match(lock_area):
                        return True
            # 다음 회전
            rotated_key = rotate_90(rotated_key)
        return False


    m = len(key)
    n = len(lock)
    
    # 자물쇠 확장 (n + 2*(m-1))
    size = n + 2 * (m - 1)
    padded_lock = [[0] * size for _ in range(size)]

    # 자물쇠 중앙 배치
    for i in range(n):
        for j in range(n):
            padded_lock[i + m - 1][j + m - 1] = lock[i][j]
            
    # 열쇠로 자물쇠를 열수 있는 지 확인
    return can_unlock()