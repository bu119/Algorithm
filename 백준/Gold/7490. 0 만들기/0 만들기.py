def evaluates_to_zero(expression):
    result = 0
    r_operand = ""
    pre_operator = "+"
    for e in expression:
        if e == " ":
            continue
        # 피연산자: 숫자 누적
        if e.isdigit():
            r_operand += e
        else:
            # 연산자: 계산
            if r_operand:
                if pre_operator == "+":
                    result += int(r_operand)
                else:
                    result -= int(r_operand)
                r_operand = ""
            pre_operator = e

    if r_operand:
        if pre_operator == "+":
            result += int(r_operand)
        else:
            result -= int(r_operand)

    if result == 0:
        return True
    return False


def dfs(num, expression_str):
    global items

    if num == n:
        # 문자열 수식 계산 -> 0 인지 확인
        if evaluates_to_zero(expression_str):
            print(expression_str)
        return

    for item in items:
        dfs(num+1, expression_str + item + str(num+1))

        
t = int(input())
items = sorted([" ", "+", "-"])
for _ in range(t):
    n = int(input())
    dfs(1, "1")
    print()