def solution(cap, n, deliveries, pickups):
    # 최소 이동 거리 저장
    answer = 0
    # 배달해야 하는 개수 저장
    delivery = 0
    # 수거해야 하는 개수 저장
    pick = 0
    # 먼 곳 부터 먼저 처리하면 최소로 탐색 가능 (뒤에서 부터 탐색)
    for i in range(n-1,-1,-1):
        # i번째 집의 배달/수거 개수를 더 함
        delivery += deliveries[i]
        pick += pickups[i]
        # 둘중에 하나라도 값이 양수이면 이 집에서 배달/수거를 수행
        # 음수면 오가는 길에 다른 집도 배달/수거 가능
        while delivery > 0 or pick > 0:
            # 배달/수거 가능한 개수만 큼 제거
            delivery -= cap
            pick -= cap
            # 왕복 거리 더하기
            answer += (i+1)*2

    return answer