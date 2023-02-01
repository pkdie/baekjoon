import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [-1 for i in range(N)]

for i in range(len(seq)):
    while stack and seq[stack[-1]] < seq[i]:
        answer[stack.pop()] = seq[i]
    stack.append(i)

print(*answer)