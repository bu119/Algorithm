import math

def solution(r1, r2):
    answer = 0
    # 한 개의 사분면만 확인하고 *4
    for x in range(1, r2 + 1):
        # r2 경계까지 가능한 최대 정수 y (큰 거는 정수로 내림)
        max_y = math.floor((r2*r2 - x*x)**(1/2)) 
        # r1 경계까지 가능한 최소 정수 y (작은 거는 정수로 올림)
        # x의 값이 r2까지 이므로, r1*r1-x*x 값이 0보다 작아질 수 있음
        min_y = math.ceil(max((r1*r1 - x*x), 0)**(1/2))
		# 가능한 y 개수
        answer += (max_y - min_y + 1)

    return answer * 4