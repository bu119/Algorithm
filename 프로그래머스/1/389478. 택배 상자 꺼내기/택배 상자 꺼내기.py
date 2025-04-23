def solution(n, w, num):
    nr, nc = -1, -1
    row = n // w + (1 if n % w else 0)
    board = [[0]*w for _ in range(row)]
    # 숫자
    i = 1
    # 밑에서 부터 채워넣음
    for r in range(row):
        # 홀수면 오 -> 왼
        if r % 2:
            col = range(w-1, -1, -1)
        # 짝수면 왼 -> 오
        else:
             col = range(w)    
        
        for c in col:
            board[row-1-r][c] = i
            # 숫자 위치 저장
            if i == num:
                nr, nc = row-1-r, c
            # 마지막 번호 상자면 탐색 종료
            if i == n:
                break
            i += 1

    answer = 0
    while 0 <= nr and board[nr][nc]:
        answer += 1
        nr -= 1   
    
    return answer