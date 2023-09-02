import sys
input = sys.stdin.readline

def check_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())
level = 0

if n:
    opinion = [int(input()) for _ in range(n)]
    opinion.sort()
    cnt = check_round(n*0.15)
    case = opinion[cnt:n-cnt]
    level = check_round(sum(case)/len(case))

print(level)