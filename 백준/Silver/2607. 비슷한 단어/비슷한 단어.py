n = int(input())
word = list(input())

ans = 0
for _ in range(n-1):
    other = list(input())
    cnt = 0
    for w in word:
        # 첫 단어 기준으로 다음 단어들 비교
        if w in other:
            # 같은 단어가 존재하면 비교 단어에서 제거
            other.remove(w)
        else:
            # 비교 단어에 존재하지 않는 기준 단어 개수
            cnt += 1
    # len(other) 기준 단어와 같은 단어를 제거하고 난 뒤에도 존재하는 비교 단어
    if cnt < 2 and len(other) < 2:
        ans += 1
print(ans)