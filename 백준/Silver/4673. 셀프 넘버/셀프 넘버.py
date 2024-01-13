def d(n):
    return n + sum(map(int, str(n)))

notSelfNum = set()
selfNum = set(range(1, 10001))
for i in range(1, 10001):
    notSelfNum.add(d(i))

selfNum = sorted(selfNum - notSelfNum)
for i in selfNum:
    print(i)