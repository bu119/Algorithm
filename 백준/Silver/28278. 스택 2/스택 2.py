import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    case = input().rstrip()
    if case[0] == '1':
        _, num = case.split()
        stack.append(num)
    elif case == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif case == '3':
        print(len(stack))
    elif case == '4':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)