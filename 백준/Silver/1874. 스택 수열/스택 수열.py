import sys

n = int(sys.stdin.readline())

stack = []
answer = []
number = 1
flag = 0

for _ in range(n):
    num = int(sys.stdin.readline())

    while number <= num:
        stack.append(number)
        answer.append("+")
        number += 1

    if stack[-1] == num:
        stack.pop(-1)
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for ans in answer:
        print(ans)