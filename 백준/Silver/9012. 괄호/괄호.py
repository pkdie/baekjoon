import sys

T = int(sys.stdin.readline())

for _ in range(T):
    word = sys.stdin.readline().strip()
    stack = []
    flag = 0
    for i in word:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                flag = 1
                break
            else:
                stack.pop()

    if not stack and flag == 0:
        print('YES')
    elif stack or flag == 1:
        print('NO')