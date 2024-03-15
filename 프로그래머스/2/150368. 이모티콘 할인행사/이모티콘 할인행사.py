# 1.이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
# 2.이모티콘 판매액을 최대한 늘리는 것.

# 할인율은 10%, 20%, 30%, 40% 
# 기준 비율 이상의 할인 이모티콘 모두 구매
# 기준 가격 이상을 이모티콘 구매에 사용하면, 구매를 모두 취소하고 플러스 서비스에 가입
# users = [기준 비율, 기준 가격]
# emoticons : 정가

# 이모티콘 플러스 서비스 가입자를 최대한 늘리면서, 이모티콘 판매액 또한 최대로 늘리는 방법
def solution(users, emoticons):
    # [이모티콘 플러스 서비스 가입 수, 이모티콘 매출액]
    answer = [0, 0]
    n = len(users)
    m = len(emoticons)
    discount_rate = []
    
    # 각 이모티콘의 할인율은 변화 가능
    def dfs(idx):
        
        if idx == m:
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
    
    # 할인율에 따른 각 사용자 비용 계산
    def check_user():
        plus_member = 0
        sales_cost = 0
        # 사용자마다 판단
        for i in range(n):
            # 각 유저의 기준 비율과 비용
            standard_rate, standard_cost = users[i]
            # 유저마다 판매액 비교
            user_cost = 0
            # 이모티콘별 판매액 체크
            for j in range(m):
                if standard_rate <= discount_rate[j]:
                    # 판매액 얼만지
                    user_cost += (100 - discount_rate[j]) * emoticons[j] // 100
                    # 기준 비용 이상인지
                    if standard_cost <= user_cost:
                        plus_member += 1
                        user_cost = 0
                        break
            # 전체 판매액에 추가
            sales_cost += user_cost
        return plus_member, sales_cost
                  
    dfs(0)
            
    return answer