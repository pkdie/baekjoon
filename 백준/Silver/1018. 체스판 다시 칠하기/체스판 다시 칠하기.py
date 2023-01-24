import sys

N, M = map(int, sys.stdin.readline().split())
origin = []
count = []

for _ in range(N):
    origin.append(sys.stdin.readline().strip())

for a in range(N - 7):
    for b in range(M - 7):
        index1 = 0 # 체스판이 W로 시작할 경우
        index2 = 0 # 체스판이 B로 시작할 경우
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if origin[i][j] != "W":
                        index1 += 1
                    if origin[i][j] != "B":
                        index2 += 1
                else:
                    if origin[i][j] != "B":
                        index1 += 1
                    if origin[i][j] != "W":
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))