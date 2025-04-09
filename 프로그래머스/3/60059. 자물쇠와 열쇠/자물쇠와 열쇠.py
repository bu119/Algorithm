from copy import deepcopy

def solution(key, lock):
    # 자물쇠 영역 내에서 열쇠와 자물쇠가 일치하는 지 확인
    def check_match(area):
        for i in range(n):
            for j in range(n):
                if area[i + m-1][j + m-1] != 1:
                    return False
        return True
    
    # 이동한 열쇠를 회전시켜 자물쇠 열 수 있는 지 체크
    def can_unlock():
        # 행과 열 모두 0 ~ m+n-2 까지 이동
        for dx in range(m + n - 1):
            for dy in range(m + n - 1):
                # 열쇠 회전
                for k in range(4):
                    # 비교할 새 자물쇠
                    lock_area = deepcopy(padded_lock)
                    for x in range(m):
                        for y in range(m):
                            # 열쇠가 이동한 위치
                            nx = x + dx
                            ny = y + dy
                            # 자물쇠에 맞춰보기
                            lock_area[nx][ny] += rotated_keys[k][x][y]
                    # 열쇠와 자물쇠가 일치하는 지 확인
                    if check_match(lock_area):
                        return True
        return False


    m = len(key)
    n = len(lock)
    # 열쇠를 이동시키기 위해 자물쇠 영역 확장(n+2*(m-1))
    padded_lock = [[0] * (n + 2 * (m - 1)) for _ in range(n + 2 * (m - 1))]
    for i in range(n):
        for j in range(n):
            padded_lock[i + m - 1][j + m - 1] = lock[i][j]
    # 회전 각도별 열쇠 저장(90도씩 시계)
    rotated_keys = {0: key, 1: [[0]*m for _ in range(m)], 2: [[0]*m for _ in range(m)], 3: [[0]*m for _ in range(m)]}
    for i in range(m):
        for j in range(m):
            rotated_keys[1][j][m-i-1] = key[i][j]
            rotated_keys[2][m-i-1][m-j-1] = key[i][j]
            rotated_keys[3][m-j-1][i] = key[i][j]
    # 자물쇠 열 수 있는 지
    return can_unlock()