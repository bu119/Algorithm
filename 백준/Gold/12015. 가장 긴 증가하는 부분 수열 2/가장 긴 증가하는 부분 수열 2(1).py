import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
increase = [0]

for num in arr:
    if increase[-1] < num:
        increase.append(num)

    elif increase[-1] > num:
        s = 0
        e = len(increase) - 1

        # num값과 같거나 큰 가장 작은 값을 찾아야 하기 때문에 일반 이분 탐색과는 조건이 살짝 다르다.
        while s < e:
            mid = (s + e) // 2

            if increase[mid] < num:
                s = mid + 1
            else:
                e = mid

        increase[e] = num

print(len(increase)-1)
