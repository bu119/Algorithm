n = int(input())
students = []
for _ in range(n):
    name, d, m, y = input().split()
    students.append((int(y), int(m), int(d), name))
students.sort()
print(students[n-1][3])
print(students[0][3])