import sys

K = int(sys.stdin.readline())
arr = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        arr.pop(-1)
    else:
        arr.append(num)
print(sum(arr))