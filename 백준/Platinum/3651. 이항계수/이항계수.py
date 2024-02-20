# 이항계수(nCk)계산 함수
# 이항계수 계산: n * (n-1) * ... * (n-k+1) // k * (k-1) * ... * 1
def nCk(n, k):
    # 분자
    numerator = 1
    # 분모
    denominator = 1
    for x in range(k):
        numerator *= (n - x)
        denominator *= (x + 1)
    return numerator // denominator

# 이항계수 성질:
# 1.nCk = nC(n-k)
# 2.k가 n//2일 때 가장 큰 값을 가진다.
m = int(input())
# 가능한 n, k 저장
result = set()
# k값이 고정되어 있을 때 k와 m을 참고하여 가능한 n값의 범위를 탐색하면서 m값이 나오는 n, k를 저장한다.
# 이분 탐색으로 m 값이 나올 수 있는 n 찾기
# mCm(=r*2) 까지만, mC(m+1)이 되지 않게!!
# k값 후보
for r in range(1, 31):
    # n값 후보
    # 1. nCk에서 nC(n//2)일 때 최대 값을 가짐
    # 2. n의 최대 값은 m
    left, right = r * 2, m
    while left <= right:
        # n 값 조정
        mid = (left + right) // 2
        num = nCk(mid, r)
        # 찾는 값이 나오면 저장
        if num == m:
            result.add((mid, r))
            result.add((mid, mid-r))
            break
        # 범위: 최소 n 증가
        elif num < m:
            left = mid + 1
        else:
            # 범위: 최대 n 감소
            right = mid - 1

# 출력
answer = sorted(result)
print(len(answer))
for i, j in answer:
    print(i, j)