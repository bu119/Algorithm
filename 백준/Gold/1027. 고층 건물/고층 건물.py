# 기울기: y의 증가량 / x의 증가량
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


n = int(input())
buildings = list(map(int, input().split()))
ans = 0
# 기울기 비교해서 보이는 빌딩 판별
for i in range(n):
    x, y = i, buildings[i]
    visible_cnt = 0

    if i > 0:
        # 왼쪽 비교
        lx, ly = i - 1, buildings[i-1]
        visible_cnt += 1
        curr_slope = slope(x, y, lx, ly)
        # 왼쪽: 기울기가 점점 작아져야 보임
        for li in range(i-2, -1, -1):
            lx, ly = li, buildings[li]
            next_slope = slope(x, y, lx, ly)
            # 기울기가 더 작으면 카운트
            if curr_slope > next_slope:
                visible_cnt += 1
                curr_slope = next_slope

    if i < n-1:
        # 오른쪽 비교
        rx, ry = i + 1, buildings[i+1]
        visible_cnt += 1
        curr_slope = slope(x, y, rx, ry)
        # 오른쪽: 기울기가 점점 커져야 보임
        for ri in range(i+2, n):
            rx, ry = ri, buildings[ri]
            next_slope = slope(x, y, rx, ry)
            # 기울기가 더 크면 카운트
            if curr_slope < next_slope:
                visible_cnt += 1
                curr_slope = next_slope

    ans = max(ans, visible_cnt)

print(ans)