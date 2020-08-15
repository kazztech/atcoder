import math

s = input()

if s == "RSR" or s == "SRS" or s == "RSS" or s == "SSR":
    print(1)
elif s == "RRS" or s == "SRR":
    print(2)
elif s == "RRR":
    print(3)
else:
    print(0)