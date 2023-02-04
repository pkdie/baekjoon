import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip().strip('[]').split(',')

    queue = deque(arr)

    cnt = 0

    if n == 0:
        queue = []

    for i in p:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if len(queue) == 0:
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    else:
        if cnt % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")