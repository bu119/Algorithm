channel = int(input())
broken_n = int(input())
if broken_n:
    broken = input().split()
else:
    broken = []

cnt = abs(channel - 100)

for number in range(1000001):

    num = str(number)
    n = len(num)

    for i in range(n):

        if num[i] in broken:
            break

        if i == n - 1:
            cnt = min(cnt, abs(number - channel) + n)

print(cnt)