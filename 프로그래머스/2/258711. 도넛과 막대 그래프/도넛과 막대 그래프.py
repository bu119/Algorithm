def solution(edges):
    # 생성한 정점, 도넛 수, 막대 수, 8자 수
    answer = [0] * 4
    # 간선 개수 저장 {a:{in:0, out:0}, ...}
    linkedCnt = dict()
    
    for a, b in edges:
        if not linkedCnt.get(a):
            linkedCnt[a] = {'in': 0, 'out': 0}

        if not linkedCnt.get(b):
            linkedCnt[b] = {'in': 0, 'out': 0}
            
        linkedCnt[a]['out'] += 1
        linkedCnt[b]['in'] += 1
    
    for v in linkedCnt:
        # 나가는 선만 있는 연결 정점 (생성한 정점)
        if linkedCnt[v]['in'] == 0 and linkedCnt[v]['out'] >= 2:
            answer[0] = v
            # 전체 그래프 개수 저장
            answer[1] = linkedCnt[v]['out']
        # 나가는 선 0개 (막대 그래프 마지막 점) 
        elif linkedCnt[v]['out'] == 0:
            answer[2] += 1
        # 나가는 선 2개 (8자 그래프 중심 점)
        elif linkedCnt[v]['out'] == 2:
            answer[3] += 1
            
    # 전체 - (막대 + 8자) = 도넛 그래프 개수
    answer[1] -= (answer[2] + answer[3])

    return answer