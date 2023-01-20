import sys

N = int(sys.stdin.readline())
points = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((y, x))
points.sort()
for point in points:
    print(point[1], point[0])