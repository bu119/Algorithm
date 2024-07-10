# 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정
# 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
# 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함

from itertools import combinations

def solution(orders, course):
    answer = []
    for cnt in course:
        # cnt개 구성이 가능한 후보의 개수 저장
        # menu = {'AC': 4, 'CDE': 3, ...}
        candidates = {}
        # 손님이 주문한 단품메뉴
        for order in orders:
            # 손님이 주문한 단품메뉴 개수가 cnt개 이상일 때만 탐색
            # cnt개 단품메뉴의 조합들
            if len(order) >= cnt:
                # 알파벳 오름차순으로 정렬하여 조합
                for comb in combinations(sorted(order), cnt):
                    # 후보에 개수 추가
                    if comb in candidates:
                        candidates[comb] += 1
                    else:
                        candidates[comb] = 1
            
        # 가능한 후보가 있고
        if candidates:
            maxV = max(candidates.values())
            # 최대 주문 메뉴의 주문 인원이 2명 이상일 때
            if maxV > 1:
                for menu, freq in candidates.items():
                    # 최대 주문 수와 빈도가 같으면 배열에 저장
                    if freq == maxV:
                        answer.append("".join(menu))

    return sorted(answer)