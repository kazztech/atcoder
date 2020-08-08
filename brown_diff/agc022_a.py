import math

s = input()

atz = list("abcdefghijklmnopqrstuvwxyz")
sL = []
for si in s:
    sL.append(atz.index(si))

print(sL)

# for i in range(26):
#     if atz[i] in s:
#         atz[i] = "-"

# nxt = ""
# for alp in atz:
#     if alp != "-":
#         nxt = alp
#         break

# print(s + nxt)