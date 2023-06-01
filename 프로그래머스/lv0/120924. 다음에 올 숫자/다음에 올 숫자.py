def solution(common):

    a,b,c = common[:3]
    d = b - a
    if d == c-b:
        answer = common[-1] + d
    else:
        r = b / a
        answer = common[-1] * r
    
    
    return answer