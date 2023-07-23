def operation_array(matrix, n):

    result = []
    maxV = 0
    for row in matrix:
        set_row = set(row)
        tmp_row = []
        for i in set_row:
            if i == 0:
                continue

            tmp_row.append((row.count(i), i))

        tmp_row.sort()
        new_row = []
        for cnt, num in tmp_row:
            new_row.append(num)
            new_row.append(cnt)

        maxV = max(len(new_row), maxV)
        result.append(new_row)

    for j in range(n):
        size = len(result[j])
        if size != maxV:
            result[j] += [0]*(maxV-size)

    return result


r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]

r -= 1
c -= 1
#  (수, 수의 등장 횟수), 수의 등장 횟수가 커지는 순
ans = 0

while True:

    cntR = len(arr)
    cntC = len(arr[0])

    if 0 <= r < cntR and 0 <= c < cntC and arr[r][c] == k:
        print(ans)
        break

    if ans > 100:
        print(-1)
        break

    if cntR == 100 and cntC == 100:
        print(-1)
        break

    if cntR >= cntC:
        arr = operation_array(arr, cntR)
    else:
        arr = operation_array(list(zip(*arr)), cntC)
        arr = list(zip(*arr))

    ans += 1