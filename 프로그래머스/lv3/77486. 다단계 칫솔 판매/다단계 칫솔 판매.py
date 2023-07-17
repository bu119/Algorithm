# from collections import deque

def distribute(v, profit):
    global answer, memberIdx, graph, n      
    
    commission = profit // 10
    
    # 수수료 1보다 작으면 분배 그만
    if commission < 1:
        answer[v] += profit
        return
    
    # 내 수익
    myProfit = profit - commission
    answer[v] += myProfit
    
    # 민호가 아니면
    if graph[v] != n:
        distribute(graph[v], commission)
        

def solution(enroll, referral, seller, amount):
    global answer, memberIdx, graph, n
    
    n = len(enroll)
    
    # 수익 저장
    answer = [0]*(n+1)    
    # 부모 저장 (민호는 n 번째 사람)
    graph = [n]*(n+1)
    
    # enroll의 인덱스에 따라 멤버 이름 저장
    # 이름으로 인덱스 찾기 가능
    memberIdx = {}
    for i in range(n):
        memberIdx[enroll[i]] = i
        
    memberIdx['center'] = n
    
    
    # 그래프 관계 (데려온 사람 번호)
    for j in range(n):
        
        if referral[j] == '-':
            # 민호가 추천인
            graph[j] = n
        else:
            graph[j] = memberIdx[referral[j]]
    
    m = len(seller)
    # 수익 계산
    for k in range(m):
        profit = amount[k] * 100
        distribute(memberIdx[seller[k]], profit)

    return answer[:-1]