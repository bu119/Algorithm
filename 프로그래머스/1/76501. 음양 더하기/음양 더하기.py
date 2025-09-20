def solution(absolutes, signs):
    answer = 0
    n = len(signs)
    for i in range(n):
        if signs[i]:
            answer += absolutes[i] 
        else:
            answer -= absolutes[i]
    return answer