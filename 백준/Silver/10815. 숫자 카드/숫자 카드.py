
n = int(input())
cards = set(input().split())
m = int(input())
check = input().split()

for num in check:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')