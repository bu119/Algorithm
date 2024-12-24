a, b = input().split()
n = len(a)
m = len(b)
ans = m+1
for i in range(m-n+1):
    sub_b = b[i:i+n]
    cnt = 0
    for j in range(n):
        # 차이 카운트
        if a[j] != sub_b[j]:
            cnt += 1
            if ans <= cnt:
                break
    ans = min(ans, cnt)
print(ans)