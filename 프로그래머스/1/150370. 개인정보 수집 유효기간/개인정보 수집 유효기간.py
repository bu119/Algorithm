def solution(today, terms, privacies):
    answer = []
    term = {}
    for i in terms:
        type, month = i.split()
        term[type] = int(month)
    
    tyy, tmm, tdd = map(int, today.split("."))
    today_day = tdd + tmm*28 + tyy*12*28
    
    for j in range(len(privacies)):
        date, type = privacies[j].split()
        yy, mm, dd = map(int, date.split("."))
        check_day = dd + mm*28 + yy*12*28 + term[type]*28
        
        if check_day <= today_day:
            answer.append(j+1)
    return answer