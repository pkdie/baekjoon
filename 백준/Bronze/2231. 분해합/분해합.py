import sys

N = int(sys.stdin.readline())
cnt = 0
for i in range(1, N):
    str_i = str(i)
    num = i
    cnt = i
    for j in str_i:
        num += int(j)
    if num == N:
        break
    else:
        cnt = 0
print(cnt)