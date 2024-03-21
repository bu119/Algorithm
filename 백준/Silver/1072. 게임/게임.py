def binarysearch(s, e, standard):
    if standard >= 99:
        return -1

    start = s
    end = e
    minV = 0
    while start <= end:
        mid = (start + end) // 2
        curr = (y+mid)*100 // (x+mid)
        # print(standard+1, curr, mid, start, end)
        if curr < standard + 1:
            start = mid+1
        else:
            end = mid-1
            minV = mid

    if minV:
        return minV
    return -1


# 게임 횟수, 이긴 횟수
x, y = map(int, input().split())
z = y*100 // x
print(binarysearch(1, 1000000000, z))