n, m = map(int, input().split())
meat = [list(map(int, input().split())) for _ in range(n)]
# 가격 기준 오름차순 정렬 -> 싼 고기들은 얼마든지 덤으로 획득 가능
# 같은 가격이 있다면, 무게 기준 내림차순 정렬 -> 같은 가격은 비용 추가
meat = sorted(meat, key=lambda x: (x[1], -x[0]))

# 최대 비용
max_val = 2147483648
# 초기 값
sum_weight = meat[0][0]
cost = meat[0][1]
ans = max_val
for i in range(1, n):
    # 무게, 가격
    weight, price = meat[i]
    # 무게 누적
    sum_weight += weight
    # 가격이 같으면 누적
    if meat[i-1][1] == price:
        cost += price
    else:
        cost = price
    # 필요한 고기 이상이면 탐색 종료
    if sum_weight >= m:
        # 같은 가격 두개 합한 것보다 그 다음 가격이 작을 수 있음
        ans = min(ans, cost)
        # 한 개 가격이면 더 이상 비교할 필요 없음
        if cost == price:
            break
            
if ans == max_val:
    ans = -1
print(ans)