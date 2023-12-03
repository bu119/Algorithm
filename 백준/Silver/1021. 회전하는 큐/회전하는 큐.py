from collections import deque

n, m = map(int, input().split())
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) : 큐
data = deque(range(1, n+1))

idx = list(map(int, input().split()))

cnt = 0
for num in idx:
    while True:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.index(num) <= len(data)//2:
                data.rotate(-1)
                cnt += 1
            else:
                data.rotate(1)
                cnt += 1

print(cnt)