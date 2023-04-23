import sys
input = sys.stdin.readline

p, m = map(int,input().split())
# 플레이어수, 정원
room = []
for _ in range(p):
    # 플레이어의 레벨 l, 닉네임 n
    l, n = input().split()
    if room:
        flag = 1
        for i in room:
            if len(i) == m:
                continue
            # 매칭가능한 방 있음
            if int(i[0][0]) - 10 <= int(l) <= int(i[0][0]) + 10:
                i.append([l,n])
                flag = 0
                break
        # 매칭 가능한 방 없음
        if flag:
            room.append([[l, n]])
    else:
        room.append([[l,n]])

for j in room:
    if len(j) == m:
        print('Started!')
    else:
        print('Waiting!')

    for k in sorted(j, key=lambda x: x[1]):
        print(*k)