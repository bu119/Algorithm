import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
ans = ''
i = 0
while arr:
    i += 1

    if i > n:
        print('NO')
        exit()

    stack.append(i)
    ans += '+'

    while stack and arr and arr[0] == stack[-1]:
        ans += '-'
        arr.pop(0)
        stack.pop()


for k in ans:
    print(k)