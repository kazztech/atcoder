import math
import itertools

n = int(input())
li = [11] * 2000  #list(map(int, input().split(" ")))

ans = 0
print(itertools.combinations(li, 3))
# for tpl in list(itertools.combinations(li, 3)):
#     a, b, c = tpl
#     if a < b + c and b < c + a and c < a + b:
#         ans += 1

print(ans)
