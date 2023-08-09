import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    max_v = price[-1]
    profit = 0
    i = n-2
    while i > -1:
        if price[i] > max_v:
            max_v = price[i]
        else:
            profit += max_v - price[i]
        i -= 1
    print(profit)