import sys

N = int(sys.stdin.readline())

cnt = 0

for _ in range(N):
    word = sys.stdin.readline().strip()
    stack = []
    for i in word:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    if len(stack) == 0:
        cnt += 1
print(cnt)