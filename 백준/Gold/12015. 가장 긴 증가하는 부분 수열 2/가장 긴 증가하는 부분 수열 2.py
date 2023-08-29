import sys
input = sys.stdin.readline

def binary_search(target):
    s = 0
    e = len(increase) - 1

    # target 값과 같거나 큰 가장 작은 값을 찾아야 하기 때문에 일반 이분 탐색과는 조건이 살짝 다르다.
    while s < e:
        mid = (s + e) // 2

        if increase[mid] == target:
            return mid

        elif increase[mid] > target:
            e = mid
        else:
            s = mid + 1

    return e


n = int(input())
arr = list(map(int,input().split()))
increase = [arr[0]]

for i in range(1, n):
    if increase[-1] < arr[i]:
        increase.append(arr[i])
    elif increase[-1] > arr[i]:
        idx = binary_search(arr[i])
        increase[idx] = arr[i]

print(len(increase))