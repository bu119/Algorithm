import sys
input = sys.stdin.readline

m, n = map(int, input().split())
# 선이 꺾어지는 횟수
if m > n:
    print((n-1) * 2+1)
else:
    print(((m-1) * 2))
    
# 끝나는 점의 좌표
if m == n:
    if m % 2:
        print(m // 2 + 1, n // 2 + 1)
    else:
        print(m // 2 + 1, n // 2)
elif m > n:
    if n % 2:
        print(n // 2 + 1 + (m-n), n // 2 + 1)
    else:
        print(n // 2 + 1, n // 2)
else:
    if m % 2:
        print(m // 2 + 1, m // 2 + 1 + (n-m))
    else:
        print(m // 2 + 1, m // 2)