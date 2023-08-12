import sys
input = sys.stdin.readline

def binary_search(start, end):
    # 숫자 값으로 탐색 한다.
    while start <= end:
        mid = (start + end) // 2
        # 분할 가능한 랜선 수 저장
        cnt = 0
        # 분할 가능한 랜선 수 구하기
        for num in lan:
            cnt += num // mid

        # 필요한 개수 이상 분할되면 시작 값을 이동
        if cnt >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end


k, n = map(int,input().split())
lan = [int(input()) for _ in range(k)]
print(binary_search(1, max(lan)))