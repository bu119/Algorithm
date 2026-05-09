def solution(n):
    answer = -1
    num = n ** (0.5)
    if num % 1 == 0:
        answer = (num + 1)**2
    return answer