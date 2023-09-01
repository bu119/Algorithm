import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # k층에 n호
    k = int(input())
    n = int(input())
    # 0층 리스트
    people = list(range(1, n+1))

    for i in range(k):  # 층 수 만큼 반복
        for j in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용)
            people[j] += people[j - 1]  # 층별 각 호실의 사람 수를 변경
    print(people[-1])  # 가장 마지막 수 출력