def switch(bulb, cnt):

    for i in range(1, n):
        # 0번 스위치를 고정하면
        # 0번을 변화 시킬수 있는건 1번 스위치 뿐이다.
        if bulb[i - 1] != result[i - 1]:
            cnt += 1
            # 스위치 누르기
            bulb[i-1] = onOff[bulb[i-1]]
            bulb[i] = onOff[bulb[i]]
            if i < n-1:
                bulb[i+1] = onOff[bulb[i+1]]

    if bulb[-1] == result[-1]:
        return cnt
    return 100001


n = int(input())
state = list(input())
result = list(input())

onOff = {'1': '0', '0': '1'}
# 첫번째 스위치 안누르고 시작
case1 = state[:]
# 첫번째 스위치를 누르고 시작
state[0] = onOff[state[0]]
state[1] = onOff[state[1]]

ans = min(switch(case1, 0), switch(state, 1))
if ans == 100001:
    print(-1)
else:
    print(ans)