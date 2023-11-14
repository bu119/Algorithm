string1 = input()
string2 = input()
n = len(string1)
m = len(string2)
lcs = [0]*m

for i in range(n):
    cnt = 0
    for j in range(m):
        if cnt < lcs[j]:
            cnt = lcs[j]
        elif string1[i] == string2[j]:
            lcs[j] = cnt + 1
print(max(lcs))