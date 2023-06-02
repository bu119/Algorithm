n = int(input())

arr = [0, 1, 2, 4]

for i in range(4, 11):
    arr.append(arr[-1] + arr[-2] + arr[-3])

for i in range(n):
    num = int(input())
    print(arr[num])