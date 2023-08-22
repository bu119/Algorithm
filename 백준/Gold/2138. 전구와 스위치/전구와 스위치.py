from copy import deepcopy

def switch(idx, bulb):

    if idx == 0:
        arr = [0, 1]
    elif idx == n-1:
        arr = [n-2, n-1]
    else:
        arr = [idx-1, idx, idx+1]

    for i in arr:
        if bulb[i] == 0:
            bulb[i] = 1
        else:
            bulb[i] = 0

    return bulb


def change(bulb, cnt):

    for k in range(1, n):
        # 0번 스위치를 고정하면
        # 0번을 변화 시킬수 있는건 1번 스위치 뿐이다.
        if bulb[k - 1] != result[k - 1]:
            bulb = switch(k, bulb)
            cnt += 1

    if bulb[-1] == result[-1]:
        return cnt
    return 100001


n = int(input())
state = list(map(int,input()))
result = list(map(int,input()))
# 첫번째 스위치 안누르고 시작
case1 = deepcopy(state)
# 첫번째 스위치를 누르고 시작
case2 = switch(0, state)

ans = min(change(case1, 0), change(case2, 1))
if ans == 100001:
    print(-1)
else:
    print(ans)
