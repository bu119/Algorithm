import sys
input = sys.stdin.readline

def dfs(idx, plus, minus, multiplication, division, result):
    global minV, maxV
    if idx == n:
        if result < minV:
            minV = result
        if result > maxV:
            maxV = result
        return

    if plus:
        dfs(idx+1, plus-1, minus,multiplication,division, result + arrA[idx])
    if minus:
        dfs(idx+1, plus,minus-1,multiplication,division, result - arrA[idx])
    if multiplication:
        dfs(idx+1, plus,minus,multiplication-1,division, result * arrA[idx])
    if division:
        if result < 0:
            dfs(idx+1, plus, minus, multiplication, division - 1, -(-result // arrA[idx]))
        else:
            dfs(idx+1, plus, minus, multiplication, division-1, result // arrA[idx])


# 수의 개수
n = int(input())
# 수열
arrA = list(map(int,input().split()))
# 연산자 개수
plus, minus, multiplication, division = map(int, input().split())

maxV = -(10**9)
minV = 10**9

dfs(1, plus, minus, multiplication, division, arrA[0])

print(maxV)
print(minV)