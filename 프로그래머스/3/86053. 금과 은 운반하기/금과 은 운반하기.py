def solution(a, b, g, s, w, t):
    start = 0
    end = (10**9) * (10**5) * 4
    answer = (10**9) * (10**5) * 4
    
    # 도시 수
    n = len(g)
    
    # 이진 탐색
    while start <= end:
        gold = 0
        silver = 0
        total = 0
        
        mid = (start + end) // 2

        for i in range(n):
            ng = g[i]
            ns = s[i]
            nw = w[i]
            nt = t[i]

            # 이동 가능 수 (왕복)
            cnt = mid // (nt * 2)
            # 이동 가능 수 (편도)
            if mid % (nt * 2) >= nt:
                cnt += 1

            # 주어지 시간 내 최대 적재 가능량 누적하기
            maxW = cnt * nw
            
            # gold 값 업데이트
            if ng < maxW:
                gold += ng
            else:
                gold += maxW

            # silver 값 업데이트
            if ns < maxW:
                silver += ns
            else:
                silver += maxW

            # total 값 업데이트
            if ng + ns < maxW:
                total += ng + ns
            else:
                total += maxW

        if total >= a + b and gold >= a and silver >= b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    
    return answer