def part(x, y, n):
    global b
    global w
    color = arr[x][y]
    for i in range(x, x+n):         # 재귀를 위해 문자로 설정
        for j in range(y, y+n):
            if arr[i][j] != color:  # 사각형에 다른 색이 존재하면 4분할
                num = n // 2
                # 1
                part(x, y, num)
                # 2
                part(x, y + num, num)
                # 3
                part(x + num, y, num)
                # 4
                part(x + num, y + num, num)
                return

    if color == 0:  # 모듀 같은 색일 때
        w += 1
        return      # 해당 사각형 탐색 끝
    else:
        b += 1
        return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
size = 2**n
b = 0
w = 0
part(0, 0, n)
print(w)
print(b)