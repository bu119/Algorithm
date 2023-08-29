n = int(input())
solution = sorted(map(int, input().split()))

s = 0
e = n-1
minV = abs(solution[s] + solution[e])
ans = [solution[s], solution[e]]

# 투포인터 알고리즘
while s < e:
    mixture = solution[s] + solution[e]
    if minV == 0:
        break

    if abs(mixture) < minV:
        minV = abs(mixture)
        ans = [solution[s], solution[e]]
    elif mixture < 0:
        s += 1
    else:
        e -= 1

print(*ans)