# 우승자에게 지급되는 상금
# 숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식이 전달
# 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출
# 연산자의 우선순위를 새로 정의할 때, 같은 순위의 연산자는 없어야 함

from itertools import permutations
from copy import deepcopy

def solution(expression):
    # +, -, * 계산
    def calculation(a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        else:
            return a * b
    
    maxReward = 0
    
    # 숫자 순서대로 저장
    operands = list(map(int, expression.replace("+", " ").replace("-", " ").replace("*", " ").split()))
    # 연산자 순서대로 저장
    operators = []
    for i in expression:
        if i in ['+', '-', '*']:
            operators.append(i)
    
    # 연산자 우선순위 경우의 수
    for priority in permutations(['+', '-', '*'], 3):
        tmpOperands = deepcopy(operands)
        tmpOperators = deepcopy(operators)
        
        # 우선순위대로
        for k in priority:
            # 연산자 k 존재할 때 까지 계산
            while k in tmpOperators:
                # 연산자 k 위치 찾기
                i = tmpOperators.index(k)
                # 계산 결과
                result = calculation(tmpOperands[i], tmpOperands[i+1], k)
                # i번째 새로운 숫자 대입
                tmpOperands[i] = result
                # i+1번쨰 숫자 삭제
                tmpOperands.pop(i+1)
                # i번째 연산자 삭제
                tmpOperators.pop(i)
                
        # 최대 상금 갱신    
        reward = abs(tmpOperands[0])
        if maxReward < reward:
            maxReward = reward
            
    return maxReward