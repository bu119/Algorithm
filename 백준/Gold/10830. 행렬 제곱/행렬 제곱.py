import sys
input = sys.stdin.readline

# 두 행렬의 곱
def matrix_mul(m1, m2):
    new_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += (m1[i][k] * m2[k][j])
            new_matrix[i][j] %= 1000
    return new_matrix


# 짝수/홀수 분할 계산
def power(m, exponent):
    # 제곱수가 값이 1이 될 때까지 재귀
    if exponent == 1:
        for x in range(n):
            for y in range(n):
                m[x][y] %= 1000
        return m

    # m^(p // 2)
    tmp = power(m, exponent // 2)

    # 제곱수가 홀수인 경우
    if exponent % 2:
        return matrix_mul(matrix_mul(tmp, tmp), m)
    else:
        # 제곱수가 짝수인 경우
        return matrix_mul(tmp, tmp)


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 행렬 제곱 계산
matrix_product = power(matrix, b)
for row in matrix_product:
    print(*row)