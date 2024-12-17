def solution(s):
    n = len(s)
    # 최소 길이 저장
    answer = n
    # 반복 간격 완전 탐색
    for k in range(1, n//2+1):
        # 압축 문자열 저장
        compressed_string = ""
        # 비교 문자열 저장
        repeating_string = s[:k]
        # 반복 개수
        cnt = 1
        # 문자열 탐색 (n+k -> 비교된 마지막 문자열 저장)
        for i in range(k, n+k, k):
            # 앞뒤 문자열이 같으면
            if repeating_string == s[i:i+k]:
                # 반복 개수 증가
                cnt += 1
            # 다르면 -> 파이썬 슬라이싱 범위 초과 범위 자동 무시
            else:
                # 개수가 반복 안될 때
                if cnt == 1:
                    compressed_string += repeating_string
                # 개수가 반복 될 때
                else:
                    compressed_string += str(cnt) + repeating_string
                # 개수 초기화
                cnt = 1
                # 반복 문자열 변경
                repeating_string = s[i:i+k]
                
        answer = min(answer, len(compressed_string))
                
    return answer