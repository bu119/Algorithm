n = list(map(int, input()))
set_num = set(n)

minV = 0

for i in set_num:
    if i == 6 or i == 9:
        cnt = n.count(6) + n.count(9)
        if cnt % 2:
            cnt = cnt // 2 + 1
        else:
            cnt //= 2
        minV = max(minV, cnt)
    else:
        minV = max(minV, n.count(i))

print(minV)