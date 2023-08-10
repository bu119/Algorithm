n = int(input())
arr = list(map(int, input().split()))
# 두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다.
# 벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
total = sum(arr)

moveB = total * 2 - arr[0]*2 - arr[1]*2
moveBarrel = total - arr[0] - arr[n-1] # 더하기 꿀벌 위치
moveA = total - arr[1] - arr[n-1] + arr[0]

ans = max(moveA, moveB, moveBarrel+arr[1])

for m in range(2,n-1):
    # 벌A 벌B(이동) 꿀통
    moveB = moveB - arr[m]*2 + arr[m-1]

    # 꿀통 벌A(이동) 벌B
    moveA = moveA + arr[m - 1] * 2 - arr[m]

    # 벌A 꿀통(이동) 벌B
    # 꿀통 위치만 두번 더 해진다.
    # moveBarrel+arr[m]

    ans = max(ans, moveA, moveB, moveBarrel+arr[m])

print(ans)