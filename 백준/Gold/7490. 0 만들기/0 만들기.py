# 문자열 수식 만들기 (모든 경우)
def dfs(n, num, expression_str, result, pre_operator, r_operand):
    # print(result)
    if num == n:
        if pre_operator == "+":
            result += int(r_operand)
        else:
            result -= int(r_operand)
        # 문자열 수식 결과 값이 0이면 수식 출력
        if result == 0:
            print(expression_str)
        return

    # " "일 때
    dfs(n, num + 1, expression_str + " " + str(num + 1), result, pre_operator, r_operand + str(num+1))

    if pre_operator == "+":
        # "+"일 때
        dfs(n, num + 1, expression_str + "+" + str(num + 1), result + int(r_operand), "+", str(num+1))
        # "-"일 때
        dfs(n, num + 1, expression_str + "-" + str(num + 1), result + int(r_operand), "-", str(num+1))
    else:
        # "+"일 때
        dfs(n, num + 1, expression_str + "+" + str(num + 1), result - int(r_operand), "+", str(num+1))
        # "-"일 때
        dfs(n, num + 1, expression_str + "-" + str(num + 1), result - int(r_operand), "-", str(num+1))


t = int(input())
# items = sorted([" ", "+", "-"])
for _ in range(t):
    n = int(input())
    dfs(n, 1, "1", 0, "+", "1")
    print()