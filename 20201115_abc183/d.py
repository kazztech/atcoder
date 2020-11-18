import math

n, w = map(int, input().split(" "))
li = [list(map(int, input().split(" "))) for _ in range(n)]

sdp = [[] for _ in range(2 * 10**5 + 1)]
for idx, l in enumerate(li):
    sdp[l[0]].append(idx)

edp = [[] for _ in range(2 * 10**5 + 1)]
for idx, l in enumerate(li):
    edp[l[1]].append(idx)

cnt = 0
for i in range(2 * 10**5 + 1):
    for sdi in sdp[i]:
        cnt += li[sdi][2]
    for edi in edp[i]:
        cnt -= li[edi][2]
    if cnt > w:
        print("No")
        exit()
print("Yes")