import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())

    # 각 단어의 위치 저장
    posi_dic = {}
    for i in range(len(w)):
        if posi_dic.get(w[i]):
            posi_dic[w[i]].append(i)
        else:
            posi_dic[w[i]] = [i]

    minV = 20001
    maxV = 0

    for posi in posi_dic.values():
        n = len(posi)
        if n < k:
            continue

        for s in range(n-k+1):
            cnt = posi[s+k-1]-posi[s]+1
            minV = min(minV, cnt)
            maxV = max(maxV, cnt)

    if maxV:
        print(minV, maxV)
    else:
        print(-1)