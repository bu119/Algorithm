s = input()
s0 = s.replace('1', ' ').split()
s1 = s.replace('0', ' ').split()
print(min(len(s0), len(s1)))