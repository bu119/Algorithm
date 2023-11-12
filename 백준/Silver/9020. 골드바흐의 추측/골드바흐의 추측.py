# 소수 판별 함수
def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


t = int(input())

for _ in range(t):
    num = int(input())  # 짝수 입력
    # 두 수 중 줄어드는 변수
    a = num // 2
    # 두 수 중 늘어나는 변수
    b = num // 2  

    for _ in range(num // 2):
        # 두 수가 소수이면 출력
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            # 소수가 아니면 두 수를 줄이고 늘리기
            a -= 1
            b += 1