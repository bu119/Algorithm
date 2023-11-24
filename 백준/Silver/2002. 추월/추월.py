import sys
input=sys.stdin.readline

n = int(input())
# 대근이는 차가 터널에 들어가는 순서대로,
daegeun = [input() for _ in range(n)]
# 영식이는 차가 터널에서 나오는 순서대로
youngsik = [input() for _ in range(n)]
# 추월 차량 개수
overtaking_cnt = 0
# 추월 차량 저장
overtaking_car = set()
# 들어간 차량 순서대로 선택
in_idx = 0
# 나온 차량 순서대로 선택
out_idx = 0
while in_idx < n and out_idx < n:

    # 들어간 차와 나온 차 순서가 같으면
    if daegeun[in_idx] == youngsik[out_idx]:
        in_idx += 1
        out_idx += 1
    else:
        # 순서가 다를 때
        # 이미 추월해서 나간 차면
        if daegeun[in_idx] in overtaking_car:
            # 이미 나간 차 이므로 다음에 들어온 차 탐색
            in_idx += 1
        else:
            # 추월한 차이면
            # 추월 차량 저장
            overtaking_car.add(youngsik[out_idx])
            # 추월 개수 추가
            overtaking_cnt += 1
            # 다음에 나온 차 탐색
            out_idx += 1

print(overtaking_cnt)