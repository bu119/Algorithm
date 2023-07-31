import sys
from collections import deque

n = int(input())

# n번 차량 통과 시간 저장
ans = [-1] * n

# a, b, c, d 위치 차량 정보
road = {'A': deque(), 'B': deque(), 'C': deque(), 'D': deque()}

# 오른쪽에 위치한 도로
rightCar = {'A': 'D', 'B': 'A', 'C': 'B', 'D': 'C'}

for i in range(n):
    t, w = input().split()

    road[w].append((int(t), i))

    # 시작 시간
    if i == 0:
        currTime = int(t)

maxV = 1000000001

while road['A'] or road['B'] or road['C'] or road['D']:

    # 남아 있는 차량의 최소 값
    minV = maxV

    # 각 도로의 방문 차량 최소 값 체크
    minVisited = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    # 현재 시각 도로에 차량 존재 하는지 체크
    isCar = {'A': False, 'B': False, 'C': False, 'D': False}

    # 교착상태 확인
    isDeadlock = 0

    for p in ['A', 'B', 'C', 'D']:
        # 값이 있을 때
        if road.get(p):
            t, _ = road[p][0]
            # 현재 가장 빠른 방문 차량
            minVisited[p] = t

            # 차량 시간 체크
            minV = min(minV, t)
            
            # 현재 교차로에 존재하는 차량 수 (각 도로 당 1) 
            if t <= currTime:
                isDeadlock += 1

        else:
            minVisited[p] = maxV

    # 교착상태 체크
    if isDeadlock == 4:
        break

    # 기다리는 차량이 없으면 현재 시간 다가 올 차량 시간으로 갱신
    if isDeadlock == 0:
        currTime = minV

    for p in ['A', 'B', 'C', 'D']:

        # 현재 시간 까지 도착한 차량이고
        if minVisited[p] <= currTime:

            # 오른쪽 위치에 차량이 현재 시간 이후에 도착
            if road.get(rightCar[p]):
                if minVisited[rightCar[p]] > currTime:
                    isCar[p] = True
            else:
                # 오른쪽 차량 존재 안함
                isCar[p] = True

    # 통과 가능한 차량에 시간 저장
    for p in ['A', 'B', 'C', 'D']:
        if isCar[p]:
            _, num = road[p].popleft()
            ans[num] = currTime

    currTime += 1

# 각 차량의 통과 시간 출력력
for k in ans:
    print(k)
