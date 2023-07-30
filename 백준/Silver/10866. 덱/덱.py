import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    case = input().rstrip()

    if case == 'pop_front':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif case == 'pop_back':
        if queue:
            print(queue.pop())
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
        push, x = case.split()
        x = int(x)
        if push == 'push_front':
            queue.insert(0,x)
        else:
            queue.append(x)