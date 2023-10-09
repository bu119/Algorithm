from itertools import combinations
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()
    minV = 13

    # 사람 수가 32이상이면 같은 mbti가 무조건 3개이상 존재
    if n > 32:
        print(0)
        continue

    # mbti 3 이상인게 존재하면 심리적인 거리는 0
    for i in set(mbti):
        if mbti.count(i) > 2:
            minV = 0
            break

    if minV == 0:
        print(minV)
        continue

    # mbti 3개 선택
    for case in set(combinations(mbti, 3)):
        c1, c2, c3 = map(set, case)
        # 3개 중 2개씩 선택
        dist = 4 - len(c1 & c2)
        dist += 4 - len(c1 & c3)
        dist += 4 - len(c2 & c3)
        # 최솟값 비교
        minV = min(minV, dist)
    print(minV)