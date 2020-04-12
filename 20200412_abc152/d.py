import math

n = int(input())
mp = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1, n + 1):
    mp[int(str(i)[0])][int(str(i)[-1])] += 1

sm = 0
for i in range(10):
    for j in range(10):
        sm += mp[i][j] * mp[j][i]

print(sm)

# c = 0
# for i in range(1, n):
#     for j in range(1, n):
#         si, sj = str(i), str(j)
#         if si[0] == sj[-1] and si[-1] == sj[0]:
#             c += 1
