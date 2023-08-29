def two_pointer(n):
    s = 0
    e = n - 1
    minV = 2000000001
    minS = 0
    minE = 0

    # 투포인터 알고리즘
    while s < e:
        mixture = solution[s] + solution[e]

        # 혼합값이 작으면 최솟값으로 갱신
        if abs(mixture) < minV:
            minV = abs(mixture)
            minS = solution[s]
            minE = solution[e]

        # 혼합값이 0이 나오면 탐색 종료
        if minV == 0:
            break

        if mixture < 0:
            s += 1
        else:
            e -= 1

    print(minS, minE)


n = int(input())
solution = sorted(map(int, input().split()))
two_pointer(n)