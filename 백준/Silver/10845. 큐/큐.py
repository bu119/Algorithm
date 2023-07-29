import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    case = input().rstrip()

    if case == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif case == 'size':
        print(len(queue))
    elif case == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif case == 'front':
        if queue:
            print(int(queue[0]))
        else:
            print(-1)
    elif case == 'back':
        if queue:
            print(int(queue[-1]))
        else:
            print(-1)

    else:
        queue.append(int(case.split()[1]))