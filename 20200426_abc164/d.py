import math

s = "2" * 1000  #input()

slen = len(s)
cnt = 0
for i in range(slen):
    for j in range(i + 3, slen):
        if int(s[i:j + 1]) % 2019 == 0:
            cnt += 1

print(cnt)