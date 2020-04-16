import math

n = int(input())
s = input()

R, G, B = s.count("R"), s.count("G"), s.count("B")
ans = R * G * B

for i in range(n):
    for j in range(n):
        c1 = i
        c2 = i + j
        c3 = i + j * 2
        if c3 >= n: break
        if c1 == c2 == c3: continue
        if s[c1] != s[c2] and s[c2] != s[c3] and s[c1] != s[c3]:
            ans -= 1

print(ans)
# 012 024 036 048
# 123 135 147 159