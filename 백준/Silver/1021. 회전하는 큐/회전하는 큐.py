import sys

def cal1():
    return deque.pop(0)

def cal2():
    global cnt
    cnt += 1
    deque.append(deque.pop(0))

def cal3():
    global cnt
    cnt += 1
    deque.insert(0, deque.pop())

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
deque = [i for i in range(1, N + 1)]
cnt = 0

for i in num:
    while True:
        if deque[0] == i:
            cal1()
            break
        else:
            if deque.index(i) < len(deque) / 2:
                while deque[0] != i:
                    cal2()
            else:
                while deque[0] != i:
                    cal3()

print(cnt)