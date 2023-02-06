import sys

stack = []
res = 1
result = 0
word = sys.stdin.readline().strip()

for i in range(len(word)):
    if word[i] == '(':
        res *= 2
        stack.append(word[i])

    elif word[i] == '[':
        res *= 3
        stack.append(word[i])

    elif word[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if word[i - 1] == '(':
            result += res
        res //= 2
        stack.pop()

    elif word[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if word[i - 1] == '[':
            result += res
        res //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)