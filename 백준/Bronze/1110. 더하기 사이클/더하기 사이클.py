n = int(input()) # 26
num = n  # 변하는 값
cnt = 0  # 몇 번 사이클인지

while True:
    a = num // 10 # 2
    b = num % 10 # 6
    c = (a + b) % 10 # 8
    num = (b * 10) + c # 68
    
    cnt += 1
    if num == n:
        break

print(cnt)