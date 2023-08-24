import sys
input=sys.stdin.readline

n = int(input())
info = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if info.get(age):
        info[age].append(name)
    else:
        info[age] = [name]

for i in sorted(info):
    for j in info[i]:
        print(i, j)