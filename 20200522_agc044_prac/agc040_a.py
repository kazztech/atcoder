import math

s = input()

li = [0 for _ in range(len(s) + 1)]

cnt = 0
for i, si in enumerate(s):
    if si == "<":
        cnt += 1
    else:
        cnt -= 1
    li[i + 1] = cnt
liMin = min(*li, 0)
li = list(map(lambda i: i - liMin, li))

li2 = [[li[0]]]
for i in range(1, len(li) - 1):
    if li[i - 1] < li[i] > li[i + 1]:
        li2[len(li2) - 1].append(li[i])
        li2.append([])
        li2[len(li2) - 1].append(li[i])
    else:
        li2[len(li2) - 1].append(li[i])
li2[len(li2) - 1].append(li[-1])

li3 = []
for li2i in li2:
    mi = min(li2i)
    li3.append(list(map(lambda x: x - mi, li2i)))
print(li3)

ans = 0
for a in li3:
    for b in a:
        ans += b

print(ans)
"""

<<<
012

<<<>>>
123210

<<>><<>>
12101210

<<<<<>
012343

< >>> << > <<<<< >>> <
1 3 2 1 5 3 1

"""