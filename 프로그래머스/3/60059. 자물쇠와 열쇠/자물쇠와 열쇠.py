from copy import deepcopy

def solution(key, lock):
    # 이동한 열쇠를 회전시켜 자물쇠 열 수 있는 지 체크
    def can_unlock():
        # 열쇠 회전
        for k in range(4):
            # 행과 열 모두 0 ~ m+n-2 까지 이동
            for dx in range(m + n - 1):
                for dy in range(m + n - 1):
                    # 비교할 새 자물쇠
                    lock_area = deepcopy(padded_lock)
                    for x in range(m):
                        # 열쇠가 이동한 행 위치
                        nx = x + dx
                        # 행위치가 자물쇠를 벗어나면 탐색 안함
                        if not (m-1 <= nx <= n+m-2):
                            continue
                        for y in range(m):
                            # 열쇠가 이동한 열 위치
                            ny = y + dy
                            # 자물쇠 범위 넘어가면 해당열 탐색 종료
                            if ny > n+m-2:
                                break
                            # 자물쇠에 맞춰보기
                            lock_area[nx][ny] += rotated_keys[k][x][y]
                    # 열쇠와 자물쇠가 일치하는 지 확인
                    if check_match(lock_area):
                        return True
        return False
    

    # 자물쇠 영역 내에서 열쇠와 자물쇠가 일치하는 지 확인
    def check_match(area):
        for i in range(n):
            for j in range(n):
                if area[i + m-1][j + m-1] != 1:
                    return False
        return True
    
    
    m = len(key)
    n = len(lock)
    # 열쇠를 이동시키기 위해 자물쇠 영역 확장(n+2*(m-1))
    padded_lock = [[0] * (n + 2 * (m - 1)) for _ in range(n + 2 * (m - 1))]
    for i in range(n):
        for j in range(n):
            padded_lock[i + m - 1][j + m - 1] = lock[i][j]
    # 회전 각도별 열쇠 저장(90도씩 시계)
    rotated_keys = {0: key}
    for cnt in range(1, 4):
        rotated_keys[cnt] = list(zip(*rotated_keys[cnt-1][::-1]))
    # 자물쇠 열 수 있는 지 확인
    return can_unlock()