import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
# A보다 작은 숫자가 몇 개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.
# A를 행으로 나눈 몫은 그 행에서 몇 개의 숫자가 A보다 작거나 같은지 알 수 있다.
start, end = 0, k
# k번째 수는 k보다 클 수 없음

while start <= end:
    # 몇 번째 인지 찾을 수
    mid = (start + end) // 2
    # 개수를 저장
    cnt = 0

    for i in range(1, n + 1):
        # n보다 큰 경우가 존재 하기 때문에 최대 n을 갖도록 해준다.
        cnt += min(mid // i, n)

    if cnt >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)