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

    for value in posi_dic.values():
        n = len(value)
        if n >= k:

            for s in range(n-k+1):
                cnt = value[s+k-1]-value[s]+1
                if minV > cnt:
                    minV = cnt
                if maxV < cnt:
                    maxV = cnt

    if maxV:
        print(minV, maxV)
    else:
        print(-1)