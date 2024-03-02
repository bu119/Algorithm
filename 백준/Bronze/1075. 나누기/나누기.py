n = int(input())
f = int(input())

new = n - n % f
if new < (n//100) * 100:
    new = (new + f) % 100
else:
    new = (new % 100) % f

if new < 10:
    print('0' + str(new))
else:
    print(new)