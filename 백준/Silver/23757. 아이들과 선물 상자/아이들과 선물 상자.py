import heapq

def ans():
    for j in w:
        gift = heapq.heappop(box)
        if gift + j < 1:
            heapq.heappush(box, gift + j)
        else:
            return 0
    return 1


n, m = map(int, input().split())
# 각 선물 상자에 들어있는 선물의 개수
c = list(map(int, input().split()))
# 각 아이가 원하는 선물의 개수
w = list(map(int, input().split()))

box = []
for i in c:
   heapq.heappush(box, -i)

print(ans())