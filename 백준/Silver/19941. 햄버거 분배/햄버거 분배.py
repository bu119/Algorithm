import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input())
ans = 0

for i in range(n):
    if arr[i] == 'P':
        s = i-k
        e = i+k+1
        if s < 0:
            s = 0
        if e > n:
            e = n

        for j in range(s, e):
            if arr[j] == 'H':
                arr[j] = 'X'
                ans += 1
                break
print(ans)