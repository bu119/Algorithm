from collections import deque
import sys
input = sys.stdin.readline

# 옆에 톱니바퀴가 같은 극인지 다른 극인지 확인하기
def check_right(cur_wheel, cur_dir):
    global move_dir

    # 오른쪽 확인
    while cur_wheel + 1 < 4:
        right_wheel = cur_wheel + 1
        # 다른 극이면?
        if cogwheel[cur_wheel][2] != cogwheel[right_wheel][6]:
            # 방향 바꿔주기
            cur_dir = change_dir[cur_dir]
            # 바뀐 방향 저장
            move_dir[right_wheel] = cur_dir
            # 다음 오른쪽 휠 탐색
            cur_wheel = right_wheel
        else:
            break

def check_left(cur_wheel, cur_dir):
    global move_dir

    # 왼쪽 확인
    while 0 <= cur_wheel - 1:
        left_wheel = cur_wheel - 1
        # 다른 극이면?
        if cogwheel[left_wheel][2] != cogwheel[cur_wheel][6]:
            # 방향 바꿔주기
            cur_dir = change_dir[cur_dir]
            # 바뀐 방향 저장
            move_dir[left_wheel] = cur_dir
            # 다음 오른쪽 휠 탐색
            cur_wheel = left_wheel
        else:
            # 같은 극이면 탐색 종료
            break


# 회전 가능한 톱니바퀴 회전
def turn_wheel():
    global cogwheel, move_dir

    for i in range(4):

        # 0이면 회전 없음
        if move_dir[i] == 0:
            continue

        if move_dir[i] == 1:
            # 시계 방향으로 회전
            cogwheel[i].appendleft(cogwheel[i].pop())
        else:
            # 반시계 방향으로 회전
            cogwheel[i].append(cogwheel[i].popleft())


# 톱니바퀴 정보 저장
cogwheel =[deque(map(int, input().rstrip())) for _ in range(4)]
# 방향 변화
change_dir = {1: -1, -1: 1}

k = int(input())
for _ in range(k):
    wheel, direction = map(int, input().split())
    wheel -= 1
    # 방향이 1이면 시계 방향, -1이면 반시계 방향
    # 회전 가능 정보 저장
    move_dir = [0] * 4
    move_dir[wheel] = direction
    # 2번위치, 6번위치 확인
    # 오른쪽 톱니 바퀴 회전 가능 정보 저장
    check_right(wheel, direction)
    # 왼쪽 톱니 바퀴 회전 가능 정보 저장
    check_left(wheel, direction)

    # 전체 톱니바퀴 회전
    turn_wheel()

# 네 톱니바퀴 점수의 합 출력
ans = 0
for k in range(4):
    # s극 이면 해당 점수를 더한다.
    # N극은 0, S극은 1
    ans += cogwheel[k][0] * (2**k)
print(ans)