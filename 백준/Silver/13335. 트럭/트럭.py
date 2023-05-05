n, w, l = map(int,input().split())
truck = list(map(int,input().split()))
# 다리 칸
bridge = [0]*w
bridgeW = 0
time = 0
while truck or bridge:
    # 시간 추가
    time += 1
    # 시간이 지나면 다리 맨 앞칸 무게 제거
    bridgeW -= bridge.pop(0)

    # 건너야 하는 트럭이 남아 있으면
    if truck:
        # 남은 트럭이 더해져 다리 하중보다 무게가 커지면 트럭 추가 안함
        if bridgeW + truck[0] > l:
            # 남은 트럭이 존재하면 0을 추가하여 다리위에 있는 트럭 보내기
            bridge.append(0)
        else:
            # 하증을 견딜수있으면
            bridge.append(truck[0])
            # 다리위 트럭 추가
            bridgeW += truck[0]
            truck.pop(0)
print(time)