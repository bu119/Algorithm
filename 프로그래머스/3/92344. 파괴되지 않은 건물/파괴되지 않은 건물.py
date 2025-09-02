def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    # 내구도 누적합용 배열 (경계+1 표기를 위해 +1 크기)
    effect = [[0]*(m+1) for _ in range(n+1)]
    
    # 내구도가 받는 영향 저장
    for t, r1, c1, r2, c2, degree in skill:
        # 적이 공격하면 degree 만큼 내구도 감소
        if t == 1:
            degree = -degree
        # 1) 시작 위치에 degree 저장 (영향 시작점)
        effect[r1][c1] += degree
        # 2) 끝 열 다음 칸에 -degree 저장 (가로 누적합 시 [c1..c2]만 유지)
        effect[r1][c2 + 1] -= degree
        # 3) 끝 행 다음 칸에 -degree 저장 (세로 누적합 시 [r1..r2]만 유지)
        effect[r2 + 1][c1] -= degree
        # 4) 대각선 모서리에 +degree 저장 (중복 상쇄를 보정)
        effect[r2 + 1][c2 + 1] += degree
             
    # 좌->우 누적합
    for i in range(n):
        for j in range(1, m):
            effect[i][j] += effect[i][j-1]

    # 상->하 누적합
    for j in range(m):
        for i in range(1, n):
            effect[i][j] += effect[i-1][j]
            
    # 최종 내구도 > 0 개수 저장
    answer = 0
    # 건물 내구도와 누적 영향력 계산 (기존 배열과 합)
    for i in range(n):
        for j in range(m):
            # 최종 내구도 > 0 개수 세기
            if board[i][j] + effect[i][j] > 0:
                answer += 1
                
    return answer