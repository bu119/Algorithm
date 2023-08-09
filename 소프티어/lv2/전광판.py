import sys

# 번호마다 스위치 표시
num = {
    'x': (False, False, False, False, False, False, False),
    '0': (True, True, True, True, True, True, False),
    '1': (False, True, True, False, False, False, False),
    '2': (True, True, False, True, True, False, True),
    '3': (True, True, True, True, False, False, True),
    '4': (False, True, True, False, False, True, True),
    '5': (True, False, True, True, False, True, True),
    '6': (True, False, True, True, True, True, True),
    '7': (True, True, True, False, False, True, False),
    '8': (True, True, True, True, True, True, True),
    '9': (True, True, True, True, False, True, True)
    }

t = int(input())
for _ in range(t):
    a, b = input().split()

    a = 'x' * (5 - len(a)) + a
    b = 'x' * (5 - len(b)) + b

    ans = 0
    for i in range(5):
        if a[i] != b[i]:
            numA = a[i]
            numB = b[i]
            for j in range(7):
                # 각 번호의 전광판 상태
                if num[numA][j] != num[numB][j]:
                    ans += 1

    print(ans)