from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다.
# 벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
ans = 0
# 완전 탐색
idx = list(combinations(range(n),2))

# 꿀통 인덱스 k
for k in range(n):
    for a,b in idx:
        # a < b
        if k == a or k == b:
            continue
        if k < a:
            # k a b
            ans = max(ans, sum(arr[k:a]) + sum(arr[k:b]) - arr[a])

        elif b < k:
            # a b k
            ans = max(ans, sum(arr[a+1:k+1]) + sum(arr[b+1:k+1]) - arr[b])
        else:
            # a k b
            ans = max(ans, sum(arr[a+1:k+1]) + sum(arr[k:b]))

print(ans)