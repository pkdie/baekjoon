import sys

xlist = []
ylist = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xlist.append(x)
    ylist.append(y)
for i in xlist:
    if xlist.count(i) == 1:
        requiredx = i
        break
for j in ylist:
    if ylist.count(j) == 1:
        requiredy = j
        break
print(requiredx, requiredy)