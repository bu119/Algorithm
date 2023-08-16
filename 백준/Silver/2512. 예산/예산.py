def binary_search(start, end):

    while start <= end:
        ssum = 0
        # 상한액 설정
        mid = (start + end) // 2

        for money in budget:
            if mid <= money:
                ssum += mid
            else:
                ssum += money

        if ssum <= m:
            # 상한액 올려야 됌
            start = mid + 1
        else:
            # 상한액 내려야함
            end = mid - 1
    return end


n = int(input())
budget = list(map(int, input().split()))
# 총 예산
m = int(input())

start = 1
end = max(budget)
print(binary_search(start, end))