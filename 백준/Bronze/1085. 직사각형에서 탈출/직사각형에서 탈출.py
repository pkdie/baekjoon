import sys

x, y, w, h = map(int, sys.stdin.readline().split())
minx = min(w - x, x)
miny = min(h - y, y)
print(min(minx, miny))