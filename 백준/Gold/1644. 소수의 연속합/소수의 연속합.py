n = int(input())

# 빠른 소수 구하기 (에라토스 테네스의 체 최적화)
arr = [True] * (n+1)
arr[0] = False
arr[1] = False
prime_num = []

for i in range(2, n+1):
    if arr[i]:
        prime_num.append(i)
        for j in range(2*i, n+1, i):
            arr[j] = False

ans = 0
start = 0
end = 0
while end <= len(prime_num):
    ssum = sum(prime_num[start:end])
    if ssum == n:
        ans += 1
        end += 1
    elif ssum < n:
        end += 1
    else:
        start += 1

print(ans)