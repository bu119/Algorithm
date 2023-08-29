def two_pointer():
    s = 0
    e = n - 1
    minV = abs(solution[s] + solution[e])
    minS = solution[s]
    minE = solution[e]

    # 투포인터 알고리즘
    while s < e:
        mixture = solution[s] + solution[e]
        if minV == 0:
            break

        if abs(mixture) < minV:
            minV = abs(mixture)
            minS = solution[s]
            minE = solution[e]
        elif mixture < 0:
            s += 1
        else:
            e -= 1

    print(minS, minE)


n = int(input())
solution = sorted(map(int, input().split()))
two_pointer()