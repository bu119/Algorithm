import sys
input = sys.stdin.readline

trees = dict()
total = 0
while True:
	tree = input().rstrip()
	if not tree:
		break

	total += 1
	if tree in trees:
		trees[tree] += 1
	else:
		trees[tree] = 1

for name in sorted(trees):
	print(f"{name} {trees[name]*100/total:.4f}")