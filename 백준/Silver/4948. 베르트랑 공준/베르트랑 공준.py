import math

n = 123456*2
prime_number = [True] * (n + 1)

# 에라토스테네스의 체 알고리즘 수행
for i in range(2, int(math.sqrt(n)) + 1):
    if prime_number[i] == True:
        j = 2
        while i * j <= n:
            prime_number[i * j] = False
            j += 1

while True:
    n = int(input())

    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if prime_number[i]:
            cnt += 1

    print(cnt)