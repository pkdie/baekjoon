from collections import deque

m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    max_value = 0
    for idx in graph:
        if 0 in idx:
            return -1
        if max(idx) > max_value:
            max_value = max(idx)
    return max_value - 1

print(bfs(graph))