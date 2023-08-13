n = int(input())
card = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

findNum = {}
for num in card:
    if num in findNum:
        findNum[num] += 1
    else:
        findNum[num] = 1

for find in check:
    if find in findNum:
        print(findNum[find], end=' ')
    else:
        print(0, end=' ')