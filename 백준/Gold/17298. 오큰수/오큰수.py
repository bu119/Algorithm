n = int(input())
a = list(map(int, input().split()))
# nge 저장
nge = [-1]*n
# 원소의 인덱스 담기
stack = [0]
for i in range(1, n):
    # a[i]가 stack에 저장된 값보다 크면
    while stack and a[stack[-1]] < a[i]:
        # stack에 저장된 nge 인덱스에 큰 수 저장
        nge[stack.pop()] = a[i]
    # a[i]보다 stack에 저장된 값이 크면 인덱스 저장
    stack.append(i)
print(" ".join(map(str, nge)))