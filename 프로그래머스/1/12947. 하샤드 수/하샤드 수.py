def solution(x):
    answer = True
    if x % sum(map(int, str(x))):
        answer = False
    return answer