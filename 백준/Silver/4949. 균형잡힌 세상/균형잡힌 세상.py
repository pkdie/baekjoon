import sys

sentence = '0'

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.':
        break
    stack = []
    answer = 0
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                answer = 1
                break
            elif stack[-1] == '(':
                stack.pop()

        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                answer = 1
                break
            elif stack[-1] == '[':
                stack.pop()

    if len(stack) == 0 and answer == 0:
        print('yes')
    elif len(stack) > 0 or answer == 1:
        print('no')