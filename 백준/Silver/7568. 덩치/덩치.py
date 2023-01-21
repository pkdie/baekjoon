import sys

N = int(sys.stdin.readline())
mass = []
score = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    mass.append((x, y))
for i in mass:
    rank = 1
    for j in mass:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")