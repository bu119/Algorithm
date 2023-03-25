# 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정
# 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
# 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함

from itertools import combinations


def solution(orders, course):
    answer = []
    for num in course:
        # 가능한 후보들
        candidates = []
        # 가능한 후보들의 개수
        cnt = {}
        for order in orders:
            candidate = combinations(sorted(order), num)
            candidates += candidate

        for case in set(candidates):
            cnt[case] = candidates.count(case)

        if cnt and max(cnt.values()) > 1:
            maxvV = max(cnt.values())
            for word in cnt:
                if maxvV == cnt[word]:
                    answer.append("".join(word))

    return sorted(answer)