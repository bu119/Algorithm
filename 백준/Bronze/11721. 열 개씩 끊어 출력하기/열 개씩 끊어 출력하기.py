string = input()
n = len(string)

for i in range(0, n, 10):
    print(string[i:i+10])