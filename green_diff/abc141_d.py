import heapq

n, m = map(int, input().split())
aL = list(map(lambda x: int(x) * (-1), input().split(" ")))

heapq.heapify(aL)

for i in range(m):
    a = heapq.heappop(aL)
    a = int(a / 2)
    heapq.heappush(aL, a)

print(int(sum(aL) * -1))

# headp
# https://qiita.com/ell/items/fe52a9eb9499b7060ed6