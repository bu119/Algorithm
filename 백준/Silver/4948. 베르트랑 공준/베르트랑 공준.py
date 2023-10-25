# 소수 찾기
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for k in range(2, int(x**(1/2) + 1)):
        # x가 해당 수로 나누어 떨어진다면
        if x % k == 0:
            return False # 소수가 아니다.
    return True # 소수이다.


while True:
    n = int(input())

    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if is_prime_number(i):
            cnt += 1

    print(cnt)