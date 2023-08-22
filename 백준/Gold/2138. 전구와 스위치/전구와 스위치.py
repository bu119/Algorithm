from copy import deepcopy

def switch(bulb, arr):

    for i in arr:
        bulb[i] = onOff[bulb[i]]

    return bulb


def change(bulb, cnt):

    for k in range(1, n):
        # 0번 스위치를 고정하면
        # 0번을 변화 시킬수 있는건 1번 스위치 뿐이다.
        if bulb[k - 1] != result[k - 1]:
            cnt += 1

            if k == n - 1:
                arr = [n - 2, n - 1]
            else:
                arr = [k - 1, k, k + 1]

            for i in arr:
                bulb[i] = onOff[bulb[i]]

    if bulb[-1] == result[-1]:
        return cnt
    return -1


n = int(input())
state = list(input())
result = list(input())

onOff = {'1': '0', '0': '1'}
# 첫번째 스위치 안누르고 시작
case1 = deepcopy(state)
cnt = change(case1, 0)

if cnt > -1:
    print(cnt)
else:
    # 첫번째 스위치를 누르고 시작
    case2 = switch(state, [0, 1])
    print(change(case2, 1))