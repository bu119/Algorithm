import sys
input = sys.stdin.readline
# 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int, input().split())
kind = []
eat = dict()

for i in range(n):
    sushi = int(input())
    kind.append(sushi)

    # k개 접시 저장
    if i < k:
        if sushi in eat:
            eat[sushi] += 1
        else:
            eat[sushi] = 1

cnt = 0
end = k-1

for start in range(n):
    # print(eat)
    eat[c] = 1
    # 최대 종류
    cnt = max(cnt, len(eat))

    # 왼쪽 제거
    eat[kind[start]] -= 1
    if eat[kind[start]] == 0:
        del eat[kind[start]]

    # 한칸 옆으로
    end = (end+1) % n
    # 오른쪽 추가
    if kind[end] in eat:
        eat[kind[end]] += 1
    else:
        eat[kind[end]] = 1

print(cnt)