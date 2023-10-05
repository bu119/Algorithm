n = int(input())
target = int(input())
arr = [[0]*n for _ in range(n)]

di = [1, 0, -1, 0]  # 하 우 상 좌
dj = [0, 1, 0, -1]

num = n**2
i = j = k = r = c = 0
arr[i][j] = num

while num > 1:

    i += di[k]
    j += dj[k]
    if 0 <= i < n and 0 <= j < n and not arr[i][j]:
        num -= 1
        arr[i][j] = num
        if num == target:
            r = i
            c = j
    else:
        i -= di[k]
        j -= dj[k]
        k = (k+1) % 4

for x in arr:
    print(' '.join(map(str, x)))
print(r+1, c+1)