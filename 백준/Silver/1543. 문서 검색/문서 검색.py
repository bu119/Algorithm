string = input()
word = input()
ans = 0
while word in string:
    ans += 1
    string = string.replace(word, "1", 1)
print(ans)