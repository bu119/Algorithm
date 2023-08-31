import sys
input = sys.stdin.readline

def vps(case):
    stack = []
    for p in case:
        if p == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
        else:
            stack.append(p)

    if stack:
        return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    ps = input().rstrip()
    print(vps(ps))