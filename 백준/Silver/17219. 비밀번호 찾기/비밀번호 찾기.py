import sys
input = sys.stdin.readline

n, m = map(int,input().split())

info = {}
for _ in range(n):
    address, password = input().split()
    info[address] = password

for _ in range(m):
    site = input().rstrip()
    print(info[site])