import sys
input = sys.stdin.readline

# x개 중에 y개 뽑기 (순서 상관x)
def com_cnt(x, y):
    numerator = 1
    denominator = 1
    for i in range(y):
        numerator *= (x-i)
        denominator *=(i+1)
    return numerator//denominator


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(com_cnt(m, n))