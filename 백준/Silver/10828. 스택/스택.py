import sys

def push(arr, num):
    arr.append(num)

def pop(arr):
    if len(arr) >= 1:
        return arr.pop(-1)
    else:
        return -1

def size(arr):
    return len(arr)

def empty(arr):
    if len(arr) == 0:
        return 1
    else:
        return 0

def top(arr):
    if len(arr) >= 1:
        return arr[-1]
    else:
        return -1

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    command = sys.stdin.readline().strip()
    if command == "pop":
        print(pop(stack))
    elif command == "size":
        print(size(stack))
    elif command == "empty":
        print(empty(stack))
    elif command == "top":
        print(top(stack))
    else:
        command, num = command.split()
        num = int(num)
        push(stack, num)