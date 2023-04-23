import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = set()
for _ in range(n):
    memo.add(input().rstrip())
for j in range(m):
    word = set(input().rstrip().split(","))
    memo -= word
    print(len(memo))