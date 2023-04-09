n, m = map(int,input().split())
posi = list(map(int,input().split()))
left = []
right = []

posi.sort()
maxV = max(abs(posi[0]), abs(posi[-1]))

for num in posi:
    if num < 0:
        left.append(abs(num))
    else:
        right.append(num)

# 내림차순
right.reverse()

ans = maxV
for i in range(0, len(left), m):
    if left[i] != maxV:
        ans += (left[i]*2)

for j in range(0, len(right), m):
    if right[j] != maxV:
        ans += (right[j]*2)

print(ans)