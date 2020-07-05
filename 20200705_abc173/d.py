import math
import collections

n = int(input())
li = list(map(int, input().split(" ")))

li = sorted(li, reverse=True)

for 


# d = collections.deque([])
# for i, l in enumerate(li):
#     if i == 0:
#         d.append(l)
#         continue
#     if d[0] > d[-1]:
#         bef = d[0]
#         d.appendleft(l)
#         aft = d[-1]
#         print(min(bef, aft))
#         ans += min(bef, aft)
#     else:
#         bef = d[-1]
#         d.append(l)
#         aft = d[0]
#         print(min(bef, aft))
#         ans += min(bef, aft)

print(ans)