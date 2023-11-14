string1 = input()
string2 = input()
n = len(string1)
m = len(string2)
lcs = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if string1[i-1] == string2[j-1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
print(lcs[n][m])