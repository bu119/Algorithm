students = set(range(1, 31))
for _ in range(28):
    n = int(input())
    students -= {n}
for i in sorted(students):
    print(i)