def solution(a, b, g, s, w, t):
    # 도시 수
    n = len(g)
    # 최소 시간
    start = 0
    # 최악의 시간: 운반가능 무게는 최소, 필요한 광물(금,은)과 트럭 당 이동시간은 최대 
    end = 1 *(10**9 * 2) * (10**5 * 2)
    # 트럭 당 운반 가능 무게(최소) * 필요한 광물 * (금, 은) * 트럭 당 편도 이동 시간(최대) * 왕복
    answer = 1 *(10**9 * 2) * (10**5 * 2)
    
    # 이분 탐색
    while start <= end:
        # 소요 시간 탐색
        mid = (start + end) // 2
        # mid 시간동안 전체 도시에서 운반한 금, 은, 금+은 총 무게 저장
        gold = 0
        silver = 0
        total = 0
        # mid 시간동안 각 도시에서 운반한 광물 계산
        for i in range(n):
            # 현재 도시에서 이동 가능한 횟수 저장 (왕복)
            cnt = mid // (t[i]*2)
            # 편도로 한번 더 갈 수 있으면 1 추가
            if mid % (t[i]*2) >= t[i]:
                cnt += 1
                
            # 현재 도시에서 이동 가능한 광물 무게
            weight = cnt * w[i]
            # 현재 도시에서 운반한 광물의 무게 누적
            gold += min(g[i], weight)
            silver += min(s[i], weight)
            total += min(g[i] + s[i], weight)
        # 필요한 무게 이동 가능하면 (운반한 금, 은, 금+은이 필요한 무게 이상인지 확인)
        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
        else:
            start = mid + 1

    return start