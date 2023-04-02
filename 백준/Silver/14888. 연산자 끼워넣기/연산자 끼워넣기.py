from itertools import permutations
import sys
input = sys.stdin.readline
def calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num1 < 0:
            ans = -num1 // num2
            ans = - ans
        else:
            ans = num1 // num2
        return ans


# 수의 개수
n = int(input())
# 수열
arrA = list(map(int,input().split()))
# 연산자 개수
operCnt = list(map(int, input().split()))
operKind = ['+', '-', '*', '/']
operations = ''
for i in range(4):
    operations += (operCnt[i]*operKind[i])
maxV = -(10**9)
minV = 10**9

for oper in permutations(operations):
    result = arrA[0]
    for j in range(1, n):
        result = calculation(result, arrA[j], oper[j-1])
    if result < minV:
        minV = result
    if result > maxV:
        maxV = result

print(maxV)
print(minV)