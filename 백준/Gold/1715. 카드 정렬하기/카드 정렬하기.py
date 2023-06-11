import sys, heapq
input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

ssum = 0
while len(card) > 1:
    num = heapq.heappop(card) + heapq.heappop(card)
    ssum += num
    heapq.heappush(card, num)

print(ssum)