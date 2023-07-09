def solution(new_id):
    # 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
    # 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천
    
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자
    # 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

    answer = ''

    for i in range(len(new_id)):
        if new_id[i].isalpha():
            answer += new_id[i].lower()
            # print("알파벳: ", new_id[i])
            
        elif new_id[i].isdigit() or new_id[i] == '-' or new_id[i] == '_':
            answer += new_id[i]
            # print("숫자와 문자들: ", new_id[i])
            
        elif new_id[i] == '.':
            # 3. 마침표(.)가 2번 이상 연속이면
            if answer and answer[-1] != '.':
                answer += new_id[i]

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    if answer and (answer[0] == '.' or answer[-1] == '.'):
        answer = answer.strip('.')
    
    # 5. 빈 문자열이라면
    if not answer:
        answer= 'a' * 3

    n = len(answer) 
    
    # 6. new_id의 길이가 16자 이상이면
    if 15 < n:
        answer = answer[:15]
    
    # 6. 마침표(.)가 끝에 위치한다면
    if answer[-1] == '.':
        answer = answer.rstrip('.')
        
    # 7. 길이가 2자 이하라면,
    if n < 3:
        answer += answer[-1]*(3-n)

    return answer