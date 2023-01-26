import sys

lenA, lenB = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
result = (A - B).union(B - A)
print(len(result))