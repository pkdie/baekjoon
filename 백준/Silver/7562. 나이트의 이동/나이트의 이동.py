from collections import deque

T = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(T):
    l = int(input()) # l은 체스판 한변의 길이
    graph = [[False] * l for _ in range(l)]
    x, y = map(int, input().split())
    graph[x][y] = True
    end_x, end_y = map(int, input().split())
    queue = deque()
    queue.append((x, y, 1))
    while queue:
        x, y, step = queue.popleft()
        if x == end_x and y == end_y:
            print(step - 1)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] == False:
                graph[nx][ny] = True
                queue.append((nx, ny, step + 1))