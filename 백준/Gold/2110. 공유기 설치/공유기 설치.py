import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

# 최소 거리
start = 1
# 최대 거리
end = house[-1] - house[0]

ans = 0

while start <= end:
    mid = (start + end) // 2
    now = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= mid + now:
            count += 1
            now = house[i]

    if count >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)