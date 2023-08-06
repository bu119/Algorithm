def is_prime_number(num):
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


n = int(input())
arr = map(int, input().split())
cnt = 0
for num in arr:
    if num == 1:
        continue
    if is_prime_number(num):
        cnt += 1

print(cnt)