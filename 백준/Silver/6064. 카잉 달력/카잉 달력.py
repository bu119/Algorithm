def calculate(m, n, x, y):
    # k를 x로 초기화
    k = x
    # k의 범위는 m*n을 넘을 수 없다.
    while k <= m * n:
        # 2개의 조건을 만족하는 k값을 찾는다.
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        # k-x가 m의 배수이기 때문에 k는 이미 x로 초기화해서 m만 더 더 해준다. (K = 10*P+3. 즉, K-3 = 10*P)
        k += m
    return -1


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(calculate(m, n, x, y))