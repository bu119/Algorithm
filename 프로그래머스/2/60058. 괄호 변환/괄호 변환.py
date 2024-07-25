# 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 되었습니다.
# 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램
from copy import deepcopy

def is_empty(string):
    # 빈문자열이다.
    if not string:
        return True
    # 빈문자열 아니다.
    return False

def separated_balance(string):
    n = len(string)
    # "(" 개수
    right = 0
    # ")" 개수
    left = 0
    # 탐색 시작
    for i in range(n):
        if string[i] == "(":
            right += 1
        else:
            left += 1
        # '(' 의 개수와 ')' 의 개수가 같다면
        if right == left:
            return string[:i+1], string[i+1:]

def is_correct(string):
    stack = []
    for st in string:
        if st == "(":
            stack.append(st)
        else:
            if not stack:
                # 올바른 문자열이 아니다.
                return False
            stack.pop()
    # 올바른 문자열이다.                    
    return True            


def solution(p):
    # 1.입력이 빈 문자열인 경우 -> 빈 문자열 반환 
    if is_empty(p):
        return p
    # 2.문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 함
    u, v = separated_balance(p)
    # 3.문자열 u가 "올바른 괄호 문자열" 이라면
    if is_correct(u):
        # 문자열 v에 대해 1단계부터 다시 수행
        return u + solution(v)
    # 문자열 u가 "올바른 괄호 문자열"이 아니라면
    answer = "(" + solution(v) + ")"
    # u의 첫 번째와 마지막 문자를 제거
    # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
    for s in u[1:-1]:
        if s == "(":
            answer += ")"
        else:
            answer += "("
    # 생성된 문자열 반환
    return answer