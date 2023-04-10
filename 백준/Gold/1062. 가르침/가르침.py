from itertools import combinations

n, k = map(int, input().split())
visited = {'a','n','t','i','c'}
words = [set(input()) for _ in range(n)]
ans = 0
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    k -= 5
    checkW = set()
    check = []
    for word in words:
        checkW |= word - visited
        check.append(word - visited)
    if len(checkW) < k:
        k = len(checkW)

    for com in combinations(checkW, k):
        cnt = 0
        c = set(com)
        for i in check:
            if not (i - c):
                cnt += 1

        if ans < cnt:
            ans = cnt
    print(ans)