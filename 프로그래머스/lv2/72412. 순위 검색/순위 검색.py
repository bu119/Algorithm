from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        information = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        infoType = information[:-1]  # info의 점수제외부분을 key로 분류
        score = int(information[-1])  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(infoType, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(score)  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [score]

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for q in query:  # query도 마찬가지로 key와 value로 분리
        queryInfo = q.replace('and','').split() # and 제거
        quType = queryInfo[:-1]
        quScore = int(queryInfo[-1])

        # while 'and' in quType:  
        #     qu_key.remove('and')
        while '-' in quType:  # - 제거
            quType.remove('-')
        quType = ''.join(quType)  # dict의 key처럼 문자열로 변경

        if quType in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[quType]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(quScore))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer