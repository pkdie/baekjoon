import sys

def push(i):
    queue.append(i)

def pop():
    global head
    if head > len(queue) - 1:
        return -1
    else:
        number = queue[head]
        head += 1
        return number

def size():
    if head > len(queue) - 1:
        return 0
    else:
        return len(queue) - head

def empty():
    if head > len(queue) - 1:
        return 1
    else:
        return 0

def front():
    if head > len(queue) - 1:
        return -1
    else:
        return queue[head]

def back():
    if head > len(queue) - 1:
        return -1
    else:
        return queue[-1]

head = 0
queue = []

N = int(sys.stdin.readline())

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
        command, num = command.split()
        push(int(num))