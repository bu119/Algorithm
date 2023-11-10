n = input()
arr = [0] * 9
# 홀수 짝수 관계 없이 개수가 알맞게 나오기 위해 1을 더한 상태에서 시작
# 3일 때 2세트 필요 / 4일 때 2세트 필요
arr[6] = 1
for i in n:
    if i == "9":
        arr[6] += 1
    else:
        arr[int(i)] += 1

arr[6] //= 2
print(max(arr))