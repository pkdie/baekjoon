import sys

N = int(sys.stdin.readline())
top_list = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_list[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, top_list[i]])

for ans in answer:
    print(ans, end=" ")