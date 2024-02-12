string = [['']*15 for _ in range(5)]
for i in range(5):
    row = list(input())
    for j in range(len(row)):
        string[i][j] = row[j]

for x in range(15):
    for y in range(5):
        if string[y][x]:
            print(string[y][x], end='')