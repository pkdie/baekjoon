import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
cnt = 0
for _ in range(N):
    S.add(sys.stdin.readline().strip())
for _ in range(M):
    check = sys.stdin.readline().strip()
    if check in S:
        cnt += 1
print(cnt)