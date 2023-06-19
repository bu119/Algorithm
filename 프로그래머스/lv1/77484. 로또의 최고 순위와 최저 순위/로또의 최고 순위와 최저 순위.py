def check(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6

    
def solution(lottos, win_nums):
    # 알아볼 수 없는 번호를 0으로 표기
    answer = []
    zeroCnt = lottos.count(0)
    set_lottos = set(lottos)
    set_win = set(win_nums)
    minV = set_lottos & set_win
    
    if len(minV) == 6:
        return [1,1]
    
    answer.append(check(len(minV)+zeroCnt))
    answer.append(check(len(minV)))
    
    return answer