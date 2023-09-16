import sys
input = sys.stdin.readline

s = set()
m = int(input())
for _ in range(m):
    op = input().rstrip()

    if op == 'all':
        s = set(range(1,21))
    elif op == 'empty':
        s = set()
    else:
        op, x = op.split()
        num = set([int(x)])
        if op == 'add':
            s |= num
        elif op == 'remove':
            if s & num:
                s -= num
        elif op == 'check':
            if s & num:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if s & num:
                s -= num
            else:
                s |= num