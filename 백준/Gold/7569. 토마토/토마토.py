from collections import deque

M, N, H = map(int, input().split())  # M은 상자의 가로 칸 수, N은 상자의 세로 칸 수

graph = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, input().split())))
    graph.append(box)

dx = [-1, 1, 0, 0, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1, 0, 0]  # 상, 하
dz = [0, 0, 0, 0, -1, 1]  # 좌, 우


def bfs():
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= H or ny >= N or nz >= M:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))

bfs()

max_value = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            max_value = max(graph[i][j][k], max_value)
print(max_value - 1)