s = input()
n = len(s)
string = set()

for i in range(n):
    for j in range(1, n+1):
        if i+j > n:
            break
        string.add(s[i:i+j])

print(len(string))