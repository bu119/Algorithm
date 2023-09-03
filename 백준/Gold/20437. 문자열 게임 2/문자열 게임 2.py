def two_pointer(n, arr):
    global minV, maxV
    s = 0
    e = 0

    while s < n-k+1 and e < n:

        if s + k - 1 == e:
            cnt = arr[e]-arr[s]+1
            minV = min(minV, cnt)
            maxV = max(maxV, cnt)
            s += 1
        e += 1


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

    for p in posi_dic:
        n = len(posi_dic[p])
        if n >= k:
            two_pointer(n, posi_dic[p])

    if maxV:
        print(minV, maxV)
    else:
        print(-1)