# 할인율은 10%, 20%, 30%, 40% 
# 기준 비율 이상의 할인 이모티콘 모두 구매
# 기준 가격 이상을 이모티콘 구매에 사용하면, 구매를 모두 취소하고 플러스 서비스에 가입
# users = [기준 비율, 기준 가격]
# emoticons : 정가

# 이모티콘 플러스 서비스 가입자를 최대한 늘리면서, 이모티콘 판매액 또한 최대로 늘리는 방법 찾기
# 우선순위
# 1.이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
# 2.이모티콘 판매액을 최대한 늘리는 것.

def solution(users, emoticons):
    # [이모티콘 플러스 서비스 가입 수, 이모티콘 매출액] 저장
    answer = [0, 0]
    # 사용자 수
    n = len(users)
    # 이모티콘 수
    m = len(emoticons)
    # 이모티콘 별 할인율 저장
    discount_rate = []
    
    # 각 이모티콘의 할인율 경우 찾기
    def dfs(idx):
        # 할인율을 모두 정하면
        if idx == m:
            # 유저별로 검사해서 결과에 따른 최대 값 갱신
            curr_member, curr_cost = check_user()
            if answer[0] < curr_member:
                answer[0] = curr_member
                answer[1] = curr_cost
            elif answer[0] == curr_member:
                if answer[1] < curr_cost:
                    answer[1] = curr_cost
            return
        
        # 할인율 적용
        for k in [10, 20, 30, 40]:
            discount_rate.append(k)
            dfs(idx+1)
            discount_rate.pop()
    
    
    # 각 할인율에 따른 각 사용자 비용 계산
    def check_user():
        plus_member = 0
        sales_cost = 0
        # 각 사용자마다 판단하기
        for i in range(n):
            # 각 유저의 기준 비율과 비용
            standard_rate, standard_cost = users[i]
            # 현재 유저의 총 판매액 저장
            user_cost = 0
            # 이모티콘별 판매액 확인
            for j in range(m):
                if standard_rate <= discount_rate[j]:
                    # 할인율을 적용한 판매액
                    user_cost += (100 - discount_rate[j]) * emoticons[j] // 100
                    # 기준 비용 이상이면 플러스 서비스 가입
                    if standard_cost <= user_cost:
                        plus_member += 1
                        user_cost = 0
                        break
                        
            # 전체 판매액에 현재 유저 판매액 추가
            sales_cost += user_cost
        return plus_member, sales_cost
    
    
    # 각 이모티콘별 할인율을 찾고 사용자에 적용하기
    dfs(0)
            
    return answer