import sys
input = sys.stdin.readline

n = int(input())
x_arr = list(map(int, input().split()))
# 중복 제거 후 오름차순 정렬
sort_arr = sorted(set(x_arr))
# 작은 수 개수 저장
cnt = {}
# 인덱스 = 작은수 개수
for i in range(len(sort_arr)):
    cnt[sort_arr[i]] = i

for x in x_arr:
    print(cnt[x], end=' ')