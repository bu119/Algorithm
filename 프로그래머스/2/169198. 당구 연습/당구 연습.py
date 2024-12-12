def solution(m, n, startX, startY, balls):
    # 항상 같은 위치에 공을 놓고 쳐서 리스트에 담긴 위치에 놓인 공을 맞춥니다.
    # 목표로한 공에 맞을 때까지 최소 얼마의 거리를 굴러가야 하는지가 궁금
    # 벽 기준으로 탐색
    answer = []
    for ballX, ballY in balls:
        # 최대 길이
        minD = (m**2 + n**2) * 2
        # 위쪽 벽
        # 수직이고 맞추려는 공이 위쪽 벽에 더 가까이 있으면 안됌
        if not (ballX == startX and ballY > startY):
            # 밑변**2 + 높이**2
            d = (ballX - startX)**2 + (ballY - 2*n+startY)**2
            minD = min(minD, d)
        
        # 아래쪽 벽
        # 수직이고 맞추려는 공이 아래쪽 벽에 더 가까이 있으면 안됌
        if not (ballX == startX and ballY < startY):
            d = (ballX - startX)**2 + (ballY + startY)**2
            minD = min(minD, d)
        # 왼쪽 벽
        # 수평이고 맞추려는 공이 왼쪽 벽에 더 가까이 있으면 안됌
        if not (ballY == startY and ballX < startX):
            d = (ballX + startX)**2 + (ballY - startY)**2
            minD = min(minD, d)
        # 오른쪽 벽
        # 수평이고 맞추려는 공이 오른쪽 벽에 더 가까이 있으면 안됌
        if not (ballY == startY and ballX > startX):
            d = (ballX - 2*m+startX)**2 + (ballY - startY)**2
            minD = min(minD, d)
        answer.append(minD)
        
    return answer