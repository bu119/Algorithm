from collections import deque

def operation(a, b):
    visited = set()
    deq = deque()
    deq.append((a, 0))
    while deq:
        num, cnt = deq.popleft()

        if num > b or num in visited:
            continue

        if num == b:
            return cnt + 1

        visited.add(num)

        deq.append((num * 2, cnt + 1))
        deq.append((num * 10 + 1, cnt + 1))

    return -1


A, B = map(int, input().split())
print(operation(A, B))