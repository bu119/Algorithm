maxV = 0
r = 1
c = 1
for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > maxV:
            maxV = row[j]
            r = i+1
            c = j+1
print(maxV)
print(r, c)