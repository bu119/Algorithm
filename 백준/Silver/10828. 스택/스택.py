import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    case = input().rstrip()

    if case == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif case == 'size':
        print(len(stack))
    elif case == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif case == 'top':
        if stack:
            print(int(stack[-1]))
        else:
            print(-1)
    else:
        stack.append(int(case.split()[1]))