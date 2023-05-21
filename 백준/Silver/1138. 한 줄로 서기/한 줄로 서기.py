n = int(input())
# 키: 4 2 1 3
# 키가 1인사람부터 왼쪽에 키큰 사람이 몇명 있는지: 2 1 1 0
arr = list(map(int,input().split()))
ans = [0]*n
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and ans[j] == 0:
            ans[j] = i+1
            break
        elif ans[j] == 0:
            cnt += 1
print(*ans)