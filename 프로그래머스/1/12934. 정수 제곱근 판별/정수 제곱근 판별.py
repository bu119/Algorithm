def solution(n):
    answer = -1
    num = n ** (0.5)
    if num == int(num):
        answer = (num + 1)**2
    return answer