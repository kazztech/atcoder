import math

n = 4000  #int(input())
s = ("R" * 1333) + ("G" * 1333) + ("B" * 1334)  #input()

R, G, B = [], [], []

for i in range(n):
    if s[i] == "R": R.append(i + 1)
    elif s[i] == "G": G.append(i + 1)
    elif s[i] == "B": B.append(i + 1)

cnt = 0
for r in R:
    for g in G:
        for b in B:
            i, j, k = sorted([r, g, b])
            if j - i != k - j:
                cnt += 1

print(cnt)
