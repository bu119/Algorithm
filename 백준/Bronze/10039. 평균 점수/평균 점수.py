ssum = 0
for i in range(5):
    score = int(input())
    if score < 40:
        ssum += 40
        continue
    ssum += score
print(ssum//5)