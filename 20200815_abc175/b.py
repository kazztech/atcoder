import math

n = int(input())
lL = sorted(list(map(int, input().split(" "))))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if len(set([lL[i], lL[j], lL[k]])) != 3:
                continue
            sm, no, lo = sorted([lL[i], lL[j], lL[k]])
            if lo < no + sm:
                ans += 1

print(ans)