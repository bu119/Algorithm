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
            num = int(i[0][0])
            maxV = num+10
            minV = num-10
            if 500 < maxV:
                maxV = 500
            if minV < 1:
                minV = 1

            # 매칭가능한 방 있음
            if minV <= int(l) <= maxV and len(i) < m:
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