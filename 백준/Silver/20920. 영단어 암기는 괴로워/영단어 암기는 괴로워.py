import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

arr = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for w, cnt in arr:
    print(w)