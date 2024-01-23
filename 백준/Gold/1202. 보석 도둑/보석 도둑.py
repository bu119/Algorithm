import sys, heapq
input = sys.stdin.readline

# 보석이 총 N개, 가방은 K개
n, k = map(int, input().split())

# 각 보석 무게 M, 가격 V
# 큰 순으로 정렬 - 뒤에서 부터 pop하려고
jewel = sorted(tuple(map(int, input().split())) for _ in range(n))
jewel.sort(reverse=True)
# 각 가방에 담을 수 있는 최대 무게 C
bagWeight = [int(input()) for i in range(k)]
# 가방 작은 순
bagWeight.sort()

stealPrice = 0
# 현재 가방에 담을 수 있는 보석 가격 저장
steal = []
# 작은 가방부터 탐색하여 가능한 보석 가격 모두 저장
for j in range(k):
    while jewel and jewel[-1][0] <= bagWeight[j]:
        # j번째 가방에 들어가는 보석이면
        jewelW, jewelP = jewel.pop()
        heapq.heappush(steal, -jewelP)
    # j번째 가방에 안 들어가거나 보석이 더 이상 없으면
    # 저장된 보석 중 제일 큰 가격 저장
    if steal:
        stealPrice -= heapq.heappop(steal)
print(stealPrice)