import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    grade = [list(map(int,input().split())) for _ in range(n)]
    grade.sort()
    top = grade[0][1]
    for i in range(1, n):
        # 작은 수가 순위 높음
        if grade[i][1] < top:
            # 순위가 높으면 높은 순위 바꾸기
            top = grade[i][1]

        else:
            # 순위가 낮으면 제거 (-1)
            n -= 1
    print(n)