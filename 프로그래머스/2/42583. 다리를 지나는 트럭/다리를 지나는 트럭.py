# 일차선 다리를 정해진 순으로 건너
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
def solution(bridge_length, weight, truck_weights):
    # 대기 트럭: truck_weights
    # 최소 시간 (초)
    time = 0
    # 다리 길이 만큼 베열 만들기
    bridge = [0] * bridge_length
    # 다리에 있는 트럭 무게 저장
    bridge_weight = 0
    
    while truck_weights:
        # 초 증가
        time += 1
        # 1.트럭 이동 (다리에서 무게 제거)
        bridge_weight -= bridge.pop(0)
        # 2.다리에 무게 여유 없으면 대기
        if bridge_weight + truck_weights[0] > weight:
            # 다리에 무게 0 넣어주기
            bridge.append(0)
            continue
        # 3.다리에 무게 여유 있으면 들어가기 (다리에 무게 추가)
        bridge_weight += truck_weights[0]
        bridge.append(truck_weights.pop(0))
        
    # 대기 트럭이 모두 다리에 올라가면 다리 무게 만큼 시간 추가 후 시간 반환
    return time + bridge_length