n = int(input())
card = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

findNum = {}
for num in card:
    if findNum.get(num):
        findNum[num] += 1
    else:
        findNum[num] = 1

for find in check:
    if findNum.get(find):
        print(findNum[find], end=' ')
    else:
        print(0, end=' ')