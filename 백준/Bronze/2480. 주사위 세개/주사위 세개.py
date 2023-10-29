num = list(map(int, input().split()))
setNum = set(num)
setCnt = len(setNum)

if setCnt == 1:
    print(10000+num[0]*1000)
elif setCnt == 2:
    for i in setNum:
        if num.count(i) == 2:
            print(1000+i*100)
else:
    print(max(num)*100)