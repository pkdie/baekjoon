import sys

def push(i):
    queue.append(i)

def pop():
    if not queue:
        return -1
    else:
        return queue.pop(0)

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def front():
    if not queue:
        return -1
    else:
        return queue[0]

def back():
    if not queue:
        return -1
    else:
        return queue[-1]

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    command = sys.stdin.readline().strip()
    if command == "pop":
        print(pop())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())
    else:
        com, num = command.split()
        push(int(num))