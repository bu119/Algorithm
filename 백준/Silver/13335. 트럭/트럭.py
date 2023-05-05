from collections import deque

n, w, l = map(int,input().split())
truck = deque(map(int,input().split()))
# 다리 칸
bridge = deque([0]*w)
time = 0
while truck or bridge:
    # 시간 추가
    time += 1
    # 시간이 지나면 다리 맨 앞칸 무게 제거
    bridge.popleft()

    # 건너야 하는 트럭이 남아 있으면
    if truck:
        # 남은 트럭이 더해져 다리 하중보다 무게가 커지면 트럭 추가 안함
        if sum(bridge) + truck[0] > l:
            # 남은 트럭이 존재하면 추가
            bridge.append(0)
        else:
            # 안크면 다리에 트럭 추가
            bridge.append(truck.popleft())
print(time)