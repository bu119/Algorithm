import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]

rope.sort()                 # 버틸 수 있는 무게를 오름차순으로 나열
ans = 0
for i in range(n):
    w = rope[i] * (n-i)     # 버티는 무게가 작은 로프 부터 * 그 이상인 남은 로프 개수
    if ans < w:
        ans = w

print(ans)