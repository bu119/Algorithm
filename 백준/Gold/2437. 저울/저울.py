n = int(input())
weights = sorted(map(int,input().split()))
# 누적합
ssum = 1

for weight in weights:
    if ssum < weight:
        break
    ssum += weight
    
print(ssum)