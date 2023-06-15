def solution(today, terms, privacies):
    tyy, tmm, tdd = map(int, today.split("."))

    answer = []
    term = {}
    for i in terms:
        type, month = i.split()
        term[type] = int(month)
   
    for j in range(len(privacies)):
        date, type = privacies[j].split()
        yy, mm, dd = map(int, date.split("."))
        
        # 유효기간 계산
        mm += term[type]
        
        if mm > 12:
            yy += mm//12
            mm %= 12
            
        if mm == 0:
            yy -= 1
            mm = 12
                
        dd -= 1
        if dd == 0:
            mm -= 1
            dd = 28
        
        if tyy > yy:
            answer.append(j+1)
        elif tyy == yy:
            if tmm > mm:
                answer.append(j+1)
            elif tmm == mm:
                if tdd > dd:
                    answer.append(j+1)
            

    return answer