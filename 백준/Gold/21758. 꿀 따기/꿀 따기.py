n = int(input())
honey = list(map(int, input().split()))
reversedHoney = honey[::-1]
total = sum(honey[1:n-1])

# 벌A 꿀통(이동) 벌B
# 꿀통 위치만 두번 더 해진다.
# 사이 값중 최대값만 비교
moveBarrel = total + max(honey[1:n-1])
# 벌A 벌B(이동) 꿀통
moveB = total * 2 - honey[1]*2 + honey[n-1]*2
# 꿀통 벌A(이동) 벌B (벌B 벌A(이동) 꿀통)
moveA = total * 2 - reversedHoney[1]*2 + reversedHoney[n-1]*2

ans = max(moveA, moveB, moveBarrel)

for m in range(2, n-1):
    moveB += honey[m-1] - honey[m]*2
    moveA += reversedHoney[m-1] - reversedHoney[m]*2

    ans = max(ans, moveB, moveA)

print(ans)