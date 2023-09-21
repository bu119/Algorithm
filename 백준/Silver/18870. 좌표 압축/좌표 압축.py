n = int(input())
coordinate = list(map(int, input().split()))
arr = sorted(set(coordinate))
cnt = {}
for i in range(len(arr)):
    cnt[arr[i]] = i

for j in coordinate:
    print(cnt[j], end = ' ')