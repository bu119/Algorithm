def solution(lottos, win_nums):
    # 알아볼 수 없는 번호를 0으로 표기
    answer = []
    check = [6,6,5,4,3,2,1]
    
    zeroCnt = lottos.count(0)
    set_lottos = set(lottos)
    set_win = set(win_nums)
    minV = set_lottos & set_win
    
    if len(minV) == 6:
        return [1,1]
    
    answer.append(check[len(minV)+zeroCnt])
    answer.append(check[len(minV)])
    
    return answer