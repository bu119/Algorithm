n, k = map(int, input().split())
# 식탁의 길이 N, 햄버거를 선택할 수 있는 거리 K
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