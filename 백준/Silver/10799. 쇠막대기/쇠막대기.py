import sys

T = sys.stdin.readline().strip()
stack = []
stick = 0
body = 0

for i in range(len(T)):
    if T[i] == '(' and T[i + 1] != ')':
        stick += 1
        body += 1
    elif T[i] == '(' and T[i + 1] == ')':
        body += stick
    elif T[i] == ')' and T[i - 1] != '(':
        stick -= 1

print(body)