k = int(input())
arr = []
for _ in range(k):
    num = int(input())
    if arr and num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))