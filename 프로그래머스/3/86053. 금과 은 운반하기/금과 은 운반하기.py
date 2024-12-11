def solution(a, b, g, s, w, t):
    
    def transport_mineral(time):
        gold = 0
        silver = 0
        total = 0
        # 해당 시간 안에 이동가능한 각 도시의 광물 합 
        for i in range(n):
            # 해당 도시 트럭이 시간 안에 몇번 이동 가능한 지
            move_cnt = time // (t[i] * 2)
            # 편도로 한번 더 이동 가능
            if time % (t[i] * 2) >= t[i]:
                move_cnt += 1
            # 이동 가능한 광물의 전체 무게
            move_weight = move_cnt * w[i]
            # 담을 수 있는 전체 무게
            total += min(g[i]+s[i], move_weight)
            # 최대로 담을 수 있는 금 무게
            gold += min(g[i], move_weight)
            # 최대로 담을 수 있는 은 무게
            silver += min(s[i], move_weight)
        # 해당 시간에서 광물이 a, b 만큼 새 도시로 이동가능 한 지 체크
        if a <= gold and b <= silver and a+b <= total:
            # 이동 가능
            return True
        # 이동 불가능
        return False
        
    
    # 도시 개수 저장
    n = len(g)
    # 각 도시의 모든 트럭은 동시에 움직임
    # 최악의 시간 -> 움직일 수 있는 무게는 최소이고, 트럭시간(왕복)은 최대이고, 가져와야하는 광물(금,은)도 최대일 때
    start = 0
    end = 1 * (10**5) * 2 * (10**9) * 2
    # 이분 탐색 (최소 시간 ~ 최대 시간 탐색)
    while start <= end:
        # 중간 시간
        mid = (start + end) // 2
        # 현재 시간에 이동 가능한 광물 계산해서 이동 가능한지 체크
        # 광물 이동 가능하면 최대 범위 줄이기
        if transport_mineral(mid):
            end = mid -1
        else:
            # 이동 불가능 하면 최소 범위 올리기
            start = mid + 1
            
    return start