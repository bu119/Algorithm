n, k = map(int, input().split())
arr = list(range(1, n+1))
idx = -1
print('<', end='')
while arr:
    idx += k
    if len(arr) <= idx:
        idx %= len(arr)
    print(arr.pop(idx), end='')
    idx -= 1
    if arr:
        print(',', end=' ')

print('>', end='')