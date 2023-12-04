price = int(input())
pay = 1000 - price
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in money:
    if pay//i:
        cnt += pay//i
        pay %= i

        if pay == 0:
            break
print(cnt)