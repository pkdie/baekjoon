from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    graph = []
    w, h = map(int, input().split())
    for _ in range(h):
        graph.append(list(input()))
    visited = [[0] * w for _ in range(h)]

    queue = deque()

    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@":
                queue.append((i, j))
                visited[i][j] = 1

    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                queue.append((i, j))
                visited[i][j] = "fire"


    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if visited[x][y] != "fire":
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    return visited[x][y]
                if graph[nx][ny] == "." and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

            if visited[x][y] == "fire":
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue
                if visited[nx][ny] == "fire" or graph[nx][ny] == "#":
                    continue
                visited[nx][ny] = "fire"
                queue.append((nx, ny))
    return "IMPOSSIBLE"

for _ in range(T):
    print(bfs())