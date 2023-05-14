import sys
input = sys.stdin.readline

n, l = map(int, input().split())
# 웅덩이 정렬
puddle = sorted(list(map(int, input().split())) for i in range(n))

ans = 0
# 마지막 판지 위치
boardPosi = 0
for s, e in puddle:
    boardPosi = max(s, boardPosi)
    diff = e - boardPosi
    cnt = (diff + l - 1) // l
    ans += cnt
    boardPosi += cnt * l

print(ans)