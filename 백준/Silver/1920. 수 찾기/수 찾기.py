import sys
input = sys.stdin.readline

n = int(input())
arr = set(input().split())

m = int(input())
check = input().split()

for i in check:
    if i in arr:
        print(1)
    else:
        print(0)