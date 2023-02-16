import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

graph = []
for _ in range(R):
    graph.append(list(sys.stdin.readline().strip()))

f_queue = deque()
j_queue = deque()

f_visited = [[0] * C for _ in range(R)]
j_visited = [[0] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
            f_visited[i][j] = 1
        if graph[i][j] == 'J':
            j_queue.append((i, j))
            j_visited[i][j] = 1

def bfs():
    while f_queue:
        x, y = f_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if f_visited[nx][ny] != 0 or graph[nx][ny] == '#':
                continue
            f_visited[nx][ny] = f_visited[x][y] + 1
            f_queue.append((nx, ny))

    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                return j_visited[x][y]
            if j_visited[nx][ny] != 0 or graph[nx][ny] == '#' or (f_visited[nx][ny] != 0 and f_visited[nx][ny] <= j_visited[x][y] + 1):
                continue
            j_visited[nx][ny] = j_visited[x][y] + 1
            j_queue.append((nx, ny))
    return 'IMPOSSIBLE'

print(bfs())