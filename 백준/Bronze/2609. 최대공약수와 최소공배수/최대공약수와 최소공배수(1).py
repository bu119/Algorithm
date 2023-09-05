# 최대공약수 구하기 (유클리드 호제법)
# 두 자연수 a,b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b)
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.

def gcd(a, b):
    while b != 0:
        # a를 b로 나눈 나머지 r
        r = a % b
        # 나머지를 활용하여 위 과정을 반복하기위해 a, b값 변경
        a = b
        b = r
    return a

# 최소공배수 구하기
# 두 정수 a,b에 대하여  a = x * gcd , b = y * gcd 이다. 
# (단, gcd는 a와 b의 최대공약수이고, x와 y는 서로 서로소 관계이다.)
# 따라서, 최소공배수는 a * b // gcd

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
