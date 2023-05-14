n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
minCost = cost[0]
total = minCost * road[0]
for i in range(1,n-1):
    if cost[i] < minCost:
        minCost = cost[i]
    total += minCost * road[i]

print(total)