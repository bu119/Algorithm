def solution(n):
    answer = []
    str_num = str(n)
    m = len(str_num)
    for i in range(m-1, -1, -1):
        answer.append(int(str_num[i]))
    return answer