def solution(chicken):
    # chicken: 시켜먹은 치킨의 수 (쿠폰 수)
    # 서비스 치킨 수
    answer = 0
    while chicken > 9:
        # 쿠폰으로 먹은 서비스 치킨 개수
        service = chicken // 10
        # 먹고 남은 쿠폰
        chicken %= 10
        # 서비스 치킨 개수 추가
        answer += service
        # 서비스 치킨 쿠폰
        chicken += service       

    return answer