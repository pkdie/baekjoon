import sys

N, M = map(int, sys.stdin.readline().split())
collection = {}

for i in range(1, N + 1):
    input = sys.stdin.readline().strip()
    collection[str(i)] = input
    collection[input] = str(i)
for _ in range(M):
    input = sys.stdin.readline().strip()
    print(collection.get(input))