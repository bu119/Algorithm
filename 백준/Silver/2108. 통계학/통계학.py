import sys
input=sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
ssum = sum(arr)

print(round(ssum/n))
print(arr[n//2])

cnt = {}
for i in arr:
    if cnt.get(i):
        cnt[i] += 1
    else:
        cnt[i] = 1
# value 값을 기준으로 내림차순으로 정렬
sort_cnt = sorted(cnt.items(), key = lambda x:(-x[1], x[0]))

if len(sort_cnt) > 1 and sort_cnt[0][1] == sort_cnt[1][1]:
    print(sort_cnt[1][0])
else:
    print(sort_cnt[0][0])
    
print(arr[n-1]-arr[0])