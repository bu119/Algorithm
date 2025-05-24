def solution(s):
    # 집합별로 리스트 형태로 만들기
    s = s.replace("{{", "")
    s = s.replace("}}", "")
    s_list = s.split("},{")
    # 집합 개수
    n = len(s_list)
    # 각 문자열 집합 형태를 진짜 집합으로 만들기 
    for i in range(n):
        s_list[i] = set(map(int, s_list[i].split(",")))
    # 집합 개수 순으로 정렬
    s_list.sort(key=lambda x: len(x))
    # 1개 집합 숫자 그대로 넣기
    answer = list(s_list[0])
    # 다음 집합과 차이로 다음에 올 숫자 가져오기
    for i in range(n-1):
        answer.append(list(s_list[i+1]-s_list[i])[0])
        
    return answer