n = int(input())
s = list(map(int, input().split()))
total = sum(s)
num = [0]*(total+2)

for i in range(1<<n):
    ssum = 0
    for j in range(n):
        if i & (1 << j):
            ssum += s[j]
    num[ssum] = 1

for k in range(1, total+2):
    if not num[k]:
        print(k)
        break