import sys
input = sys.stdin.readline

n = int(input()) # 공의 개수
posi = list(map(int,input().split())) # 각 공의 위치
t = int(input()) # 시간

posi.sort()
cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        if (posi[j]-posi[i]) <= 2*t:
            cnt += 1

print(cnt/4)