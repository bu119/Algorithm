def solution(wallet, bill):
    answer = 0
    br, bc = bill
    min_w = min(wallet)
    max_w = max(wallet)
    while min_w < min(br, bc) or max_w < max(br, bc):
        # 길이가 긴 쪽 반으로 접기
        if br > bc:
            br //= 2
        else:
            bc //= 2
        # 접은 횟수 추가
        answer += 1
    return answer