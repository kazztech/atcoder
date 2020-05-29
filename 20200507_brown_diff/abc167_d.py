import math

n, k = map(int, input().split(" "))
li = list(map(int, input().split(" ")))

fk = k
crnt = 1
st = set()
wl = []
key = crnt
cy = 0
mg = 0

for i in range(n):
    if crnt in st:
        key = crnt
        cy = i - wl.index(crnt)
        mg = wl.index(crnt)
        break
    st.add(crnt)
    wl.append(crnt)
    crnt = li[crnt - 1]

k -= mg
if cy != 0:
    k %= cy
crnt = key
if n > fk:
    k = fk
    crnt = 1
for i in range(k):
    crnt = li[crnt - 1]

print(crnt)
