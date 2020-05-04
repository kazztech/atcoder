import math

n, m = map(int, input().split(" "))

start = 1
end = n

_set = set()

for _ in range(m):
    _abs = min(end - start, start + n - end)
    if _abs in _set:
        end -= 1
    print(start, end, min(end - start, start + n - end))
    _set.add(_abs)
    start += 1
    end -= 1

# とけんかった