import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        # distance1은 출발점과 행성계 중심 사이의 거리
        distance1 = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        # distance2는 도착점과 행성계 중심 사이의 거리
        distance2 = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5
        if (distance1 < r and distance2 > r) or (distance1 > r and distance2 < r):
            cnt += 1
    print(cnt)