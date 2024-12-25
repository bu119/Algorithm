def is_consistent(number):
    for i in range(n-1):
        if number[i] == number[i+1][:len(number[i])]:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    phone_number = sorted(input() for _ in range(n))
    print(is_consistent(phone_number))