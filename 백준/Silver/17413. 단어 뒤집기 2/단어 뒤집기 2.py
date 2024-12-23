# 예시) <ab cd>ef gh<ij>
s = input().split("<")
# 예시) [ab cd>ef gh, ij>]
ans = ""
for string in s:
    # 예시) ab cd>ef gh
    # 태그 존재
    if ">" in string:
        # 태그, 단어 분리
        tag, string = string.split(">")
        # 예시) ab cd, ef gh
        # 태그 저장
        ans += "<" + tag + ">"
        # 예시) <ab cd>
    # 단어 분리 -> 뒤집기
    words = string.split()
    # 예시) [ef, gh]
    ans += " ".join(w[::-1] for w in words)
    # 예시) fe hg
print(ans)