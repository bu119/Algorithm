def mod(a, b):
    # b의 값이 1이면 a % c를 return
    if b == 1:
        return a % c
    else:
        # a^(b // 2)를 미리 구한다.
        tmp = mod(a, b // 2)

        if b % 2 == 0:
            # b가 짝수인 경우
            return tmp * tmp % c
        else:
            # b가 홀수인 경우
            return tmp * tmp * a % c


a, b, c = map(int, input().split())
print(mod(a,b))