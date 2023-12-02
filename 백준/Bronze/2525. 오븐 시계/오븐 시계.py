a, b = map(int, input().split())
c = int(input())

minute = (b+c) % 60
hour = (a + (b+c) // 60) % 24

print(hour, minute)