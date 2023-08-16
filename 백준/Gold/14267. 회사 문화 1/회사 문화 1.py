import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 직원 번호 인덱스 통일
superior = [0] + list(map(int, input().split()))

compliment = [0]*(n+1)

for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

for i in range(1, n + 1):
    # 사장이 아닐 때 칭찬 수치 계산
    if i != 1:
        # 상사가 가지고 있는 칭찬 수치를 부하직원에게 추가해줌
        compliment[i] += compliment[superior[i]]
        
    print(compliment[i], end=' ')