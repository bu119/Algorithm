import sys
from collections import deque

# 조직도의 높이 H, 말단에 대기하는 업무의 개수 K, 업무가 진행되는 날짜 수 R
h, k, r = map(int, input().split())

tree = [{'left':deque(), 'right':deque()} for _ in range(2**(h+1))]

# 말단 직원 업무 정보 저장
for i in range(2**h, 2**(h+1)):
    tree[i] = deque(map(int, input().split()))

for day in range(1,r+1):

    # 직원 업무 처리하기
    for j in range(1,2**h):
        v = j // 2

        # 홀수 번째 날, 왼쪽 부하 직원이 올린 처리 건이 있을 때
        if day % 2 == 1 and tree[j]['left']:
            # 상사 기준
            if j % 2 == 0:
                # 상사 기준 왼쪽 부하 직원이 올린 업무 처리 건이면 왼쪽으로 올리기
                tree[v]['left'].append(tree[j]['left'].popleft())
            else:
                # 상사 기준 오른쪽 부하 직원이 올린 업무 처리 건
                tree[v]['right'].append(tree[j]['left'].popleft())

        # 짝수 번째 날, 오른쪽 부하 직원이 올린 처리 건이 있을 때
        elif day % 2 == 0 and tree[j]['right']:
            # 왼쪽 직원 업무 처리건이면 오른쪽으로 올리기
            if j % 2 == 0:
                tree[v]['left'].append(tree[j]['right'].popleft())
            else:
                tree[v]['right'].append(tree[j]['right'].popleft())

    # 말단 직원 업무 처리해서 상사에게 올리기
    if day < k+1:
        for j in range(2**h, 2**(h+1)):
            v = j // 2

            if j % 2 == 0:
                # 상사 왼쪽 부하 직원 정보에 저장
                tree[v]['left'].append(tree[j].popleft())
            else:
                # 상사 오른쪽 부하 직원 정보에 저장
                tree[v]['right'].append(tree[j].popleft())

print(sum(tree[0]['left']) + sum(tree[0]['right']))
