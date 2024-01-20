s = input()
s0 = s.split('1')
s1 = s.split('0')
cnt0 = 0
cnt1 = 0
for i in s0:
    if i != '':
        cnt0+=1
for j in s1:
    if j != '':
        cnt1 += 1
print(min(cnt0, cnt1))