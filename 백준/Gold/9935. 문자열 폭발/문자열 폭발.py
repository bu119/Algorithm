string = input() # mirkovC4nizCC44
explosion = list(input()) # C4
n = len(string)
m = len(explosion)
stack = []
for i in range(n):
    stack.append(string[i])

    if stack[-m:] == explosion:
        for _ in range(m):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")