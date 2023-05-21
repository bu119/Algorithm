n = int(input())
# 키: 4 2 1 3
# 키가 1인사람부터 왼쪽에 키큰 사람이 몇명 있는지: 2 1 1 0
arr = list(map(int,input().split()))
ans = []
for i in range(len(arr)-1, -1, -1):
    ans.insert(arr[i], i+1)
print(*ans)