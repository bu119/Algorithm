# 기본점수, 외부 링크 수, 링크점수, 매칭점수
# 기본점수: 해당 웹페이지의 텍스트 중, 검색어가 등장하는 횟수 (대소문자 무시)
# 외부 링크 수: 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수
# 링크점수: 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수의 총합
# 매칭점수: 기본점수와 링크점수의 합으로 계산
# 매칭점수가 가장 높은 웹페이지의 index를 구하라.
# 검색어 word
# 웹페이지의 HTML 목록인 pages

import re
 
# 각 페이지마다 url, 기본점수, 링크의 수, 링크들
def seperate(word, page):
    # 기본점수 구하기
    # 해당 웹페이지의 텍스트 중, 검색어가 등장하는 횟수이다. (대소문자 무시)
    basicScore = 0
    # r'[a-zA-Z]+': 소문자와 대문자를 포함한 모든 영어 알파벳
    for w in re.findall(r'[a-zA-Z]+', page.lower()):
        # w: 영어 알파벳으로 이루어진 연속된 문자열
        if w == word.lower():
            basicScore += 1
            
    # \S: 공백이 아닌 모든 문자
    # +: 하나 이상의 공백이 아닌 문자가 연속해서 나타날 수 있음
    # () : 괄호 안의 내용을 캡처하여 나중에 사용 가능
    # 정규식에서 괄호 ()로 묶인 부분을 캡처 그룹
    # group(0): 전체 매치된 문자열을 반환
    # group(1): 첫 번째 괄호로 묶인 부분의 값만 반환
    url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
    
    # 외부 링크 수 구하기
    # 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수
    
    # https://: 링크의 시작 부분을 지정
    # [\S]*: 공백이 아닌 문자가 0개 이상 연속해서 나타날 수 있음
    # re.findall 함수: 매치된 전체를 리스트로 반환
    exLinks = re.findall('<a href="(https://[\S]*)"', page)
    # url, 기본점수, 외부 링크 수, 모든 외부 링크, 링크점수
    return url, basicScore, exLinks
    
    
def solution(word, pages):
    n = len(pages)
    # url: [인덱스, 기본점수, 외부 링크 수, 모든 외부 링크, 링크점수]
    pagesInfo = dict()

    for i in range(n):
        # 웹페이지
        page = pages[i]
        url, basicScore, exLinks = seperate(word, page) 
        # url: [인덱스, 기본점수, 외부 링크 수, 모든 외부 링크, 링크점수]
        pagesInfo[url] = [i, basicScore, len(exLinks), set(exLinks), 0]
    
    # 각 페이지의 링크점수 구하기 
    for currUrl in pagesInfo:
        # 해당 웹페이지로 외부 링크가 걸린 웹페이지 찾기
        for checkingUrl in pagesInfo:
            _, basicScore, linkNum, linkedUrls, _ = pagesInfo[checkingUrl]
            if currUrl in linkedUrls:
                pagesInfo[currUrl][4] += basicScore / linkNum
    # 매칭점수로 정렬
    sortedMatching = sorted(pagesInfo.values(), key=lambda x: -(x[1]+x[4]))
    return sortedMatching[0][0]
    