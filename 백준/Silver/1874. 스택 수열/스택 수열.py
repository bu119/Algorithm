n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
ans = ''
i = 1

for num in arr:

    while i <= num:
        stack.append(i)
        ans += '+'
        i += 1

    if stack.pop() != num:
        print('NO')
        exit()

    ans += '-'

for k in ans:
    print(k)
