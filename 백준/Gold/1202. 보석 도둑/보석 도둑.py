import sys, heapq
input = sys.stdin.readline

# 보석이 총 N개, 가방은 K개
n, k = map(int, input().split())

# 각 보석 무게 M, 가격 V
# 큰 순으로 정렬 - 뒤에서 부터 pop하려고
jewels = dict()
for _ in range(n):
    m, v = map(int, input().split())
    if jewels.get(m):
        jewels[m].append(v)
    else:
        jewels[m] = [v]
# 보석 무게만 저장
jewelsW = sorted(jewels, reverse=True)

# 각 가방에 담을 수 있는 최대 무게 C
bagWeight = [int(input()) for i in range(k)]
# 가방 작은 순
bagWeight.sort()

stealPrice = 0
# 현재 가방에 담을 수 있는 보석 가격 저장
steal = []
# 작은 가방부터 탐색하여 가능한 보석 가격 모두 저장
for j in range(k):
    # j번째 가방에 들어가는 보석이면
    while jewelsW and jewelsW[-1] <= bagWeight[j]:
        jw = jewelsW.pop()
        # 보석 가격 저장
        for jp in jewels[jw]:
            heapq.heappush(steal, -jp)
    # j번째 가방에 안 들어가거나 보석이 더 이상 없으면
    # 저장된 보석 중 제일 큰 가격 저장
    if steal:
        stealPrice -= heapq.heappop(steal)
print(stealPrice)