s = input()
n = len(s)

suffixes = []
for i in range(n):
    suffixes.append(s[i:])
suffixes.sort()

for suffix in suffixes:
    print(suffix)