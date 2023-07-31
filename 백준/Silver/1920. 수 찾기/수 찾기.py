import sys
input = sys.stdin.readline

def binary_search(start, end, x):
    if start > end:
        return 0

    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if arr[mid] == x:
        return 1
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif arr[mid] > x:
        return binary_search(start, mid - 1, x)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(mid + 1, end, x)


n = int(input())
arr = sorted(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for i in check:
    print(binary_search(0, n-1, i))