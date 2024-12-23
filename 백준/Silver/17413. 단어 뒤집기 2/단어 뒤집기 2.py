s = input()
ans = ""
# "<"가 등장하면 True
tag_flag = False
# 단어 저장 -> 뒤집기
string = ""
for char in s:
    # 태그 ("<"를 만나면 시작)
    if tag_flag:
        # 태그는 바로 저장 ("<" 도 그대로 저장)
        ans += char
    # 단어
    else:
        # 태그 시작 or 공백 -> 새로운 단어 시작
        if char == "<" or char == " ":
            # 단어 뒤집기
            ans += string[::-1]
            # 저장된 단어 초기화
            string = ""
            # "<" or " " 그대로 저장
            ans += char
        else:
            # 단어 저장
            string += char

    if char == "<" or char == ">":
        tag_flag = not tag_flag

if string:
    ans += string[::-1]

print(ans)