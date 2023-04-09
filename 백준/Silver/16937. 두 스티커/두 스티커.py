from itertools import permutations
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
sticker = []

for _ in range(n):
    r, c = map(int, input().split())
    if (r <= h and c <= w) or (c <= h and r <= w):
        sticker.append((r, c))

choice = list(permutations(sticker, 2))

ans = 0
for a, b in choice:
    x, y = a
    p, q = b
    area = 0
    if (x + p <= h and y <= w and q <= w) or (x <= h and p <= h and y + q <= w):
        area = x * y + p * q
    elif (y + p <= h and x <= w and q <= w) or (y <= h and p <= h and x + q <= w):
        area = x * y + p * q
    elif (y + q <= h and x <= w and p <= w) or (y <= h and q <= h and x + p <= w):
        area = x * y + p * q
    elif (x + q <= h and y <= w and p <= w) or (x <= h and q <= h and y + p <= w):
        area = x * y + p * q

    if ans < area:
        ans = area

print(ans)