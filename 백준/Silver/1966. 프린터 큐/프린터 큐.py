from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    deq = deque(list(map(int,input().split())))
    while deq:
        maxV = max(deq)
        num = deq.popleft()
        # 찾아야 하는 위치
        m -= 1
        # 젤 큰 수를 뽑으면
        if num == maxV:
            # 인쇄
            cnt += 1
            #  찾아야 하는 숫자를 뽑으면
            if m < 0:
                break
        else:
            # 뽑은 숫자가 큰 수가 아니면 젤 뒤로
            deq.append(num)
            # 찾아야 하는 숫자를 뽑으면
            if m < 0:
                # 맨뒤 idx
                m = len(deq) - 1

    print(cnt)