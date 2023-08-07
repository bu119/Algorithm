import sys
input = sys.stdin.readline

n, m = map(int,input().strip().split())
book = dict()
for i in range(1,n+1):
    name = input().strip()
    book[name] = i
    book[str(i)] = name

for j in range(m):
    find = input().strip()
    print(book[find])