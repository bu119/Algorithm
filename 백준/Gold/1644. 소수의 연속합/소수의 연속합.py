n = int(input())

# 빠른 소수 구하기 (에라토스 테네스의 체 최적화)
is_prime_num = [True] * (n+1)
is_prime_num[0] = False
is_prime_num[1] = False
prime_num = []

for i in range(2, n+1):
    if is_prime_num[i]:
        prime_num.append(i)
        for j in range(2*i, n+1, i):
            is_prime_num[j] = False

cnt = 0
start = 0
end = 0
ssum = 0

while True:
    if ssum >= n:
        ssum -= prime_num[start]
        start += 1
    elif end == len(prime_num):
        break
    else:
        ssum += prime_num[end]
        end += 1

    if ssum == n:
        cnt += 1

print(cnt)