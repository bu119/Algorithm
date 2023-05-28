n = int(input())
m = int(input())

s = input()
p = 'IOI'
for i in range(1,n):
    p += 'OI'

size = len(p)
cnt = 0
for j in range(m-size+1):
    if s[j:j+size] == p:
        cnt += 1

print(cnt)