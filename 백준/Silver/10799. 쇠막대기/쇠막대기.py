iron_rod = input()
stack = []
cnt = 0
for i in range(len(iron_rod)):
    if iron_rod[i] == "(":
        stack.append("(")
    else:
        if iron_rod[i - 1] == "(":
            stack.pop()
            # 첫 번째 경우인 현재의 쇠막대기 카운팅
            cnt += len(stack)

        else:
            stack.pop()
            # 두 번째 경우인 나머지 부분을 카운팅
            cnt += 1  
print(cnt)