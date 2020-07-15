import bisect

n = int(input())
li = sorted(list(map(int, input().split(" "))), reverse=True)
rLi = list(reversed(li))

ans = 0
for i in range(n - 1):
    s1 = li[i]
    for j in range(i + 1, n - 1):
        
        s2 = li[j]
        lim = s1 - s2
        print(s1, s2)
print(ans)
