def solution(dartResult):
    # 세 차례 던져 그 점수의 합계
    # 점수 계산 로직
    dart = []
    cnt = 0
    n = len(dartResult)
    i = 0
    while i < n:
        # 숫자이면 다트 새 세트 시작
        score = ""
        while i < n and dartResult[i].isdigit():
            score += dartResult[i]
            i += 1
            
        if score:
            now_score = int(score)
            dart.append(now_score)
            
        # 보너스이면
        if i < n and dartResult[i] in {'S', 'D', 'T'}:
            if dartResult[i] == "D":
                dart[cnt] = now_score**2
            elif dartResult[i] == "T":
                dart[cnt] = now_score**3
            
            i += 1    
                
        # 옵션이면    
        if i < n and dartResult[i] in {'*', '#'}:
            if dartResult[i] == "*":
                dart[cnt] *= 2
                # 2번째이상의 세트면
                if cnt > 0:
                    dart[cnt-1] *= 2
            else:
                dart[cnt] = -dart[cnt]
                
            i += 1
        
        cnt += 1
    answer = sum(dart)
    print(dart)
    return answer