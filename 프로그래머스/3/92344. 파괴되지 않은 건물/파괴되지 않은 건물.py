def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    # 처음과 끝에 +degree, -degree 저장
    effect = [[0]*(m+1) for _ in range(n+1)] 
    for t, r1, c1, r2, c2, degree in skill:
        # 적이 공격하면 degree 만큼 감소
        if t == 1:
            degree = -degree
        # 처음과 끝 위치에 degree 영향력 저장
        effect[r1][c1] += degree
        effect[r1][c2+1] -= degree
        effect[r2+1][c1] -= degree
        effect[r2+1][c2+1] += degree
             
    # 좌우 누적합
    for i in range(n):
        for j in range(1, m):
            effect[i][j] += effect[i][j-1]

    # 상하 누적합
    for j in range(m):
        for i in range(1, n):
            effect[i][j] += effect[i-1][j]
            
    # 전체 건물 내구도와 누적 영향력 계산        
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + effect[i][j] > 0:
                answer += 1
                
    return answer