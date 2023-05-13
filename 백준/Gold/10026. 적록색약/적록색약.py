import copy

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(input()))
M = len(graph[0])  # N은 세로 길이, M은 가로 길이
graph_1 = copy.deepcopy(graph)
for i in range(N):
    for j in range(M):
        if graph_1[i][j] == "G":
            graph_1[i][j] = "R"

graph1 = [[0] * M for _ in range(N)]
graph2 = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs1(x, y):
    if graph1[x][y] == 1:
        return False
    stack = []
    stack.append((x, y))
    graph1[x][y] = 1
    while stack:
        x, y = stack.pop()
        color = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph1[nx][ny] == 0 and color == graph[nx][ny]:
                graph1[nx][ny] = 1
                stack.append((nx, ny))
    return True

def dfs2(x, y):
    if graph2[x][y] == 1:
        return False
    stack = []
    stack.append((x, y))
    graph2[x][y] = 1
    while stack:
        x, y = stack.pop()
        color = graph_1[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph2[nx][ny] == 0 and color == graph_1[nx][ny]:
                graph2[nx][ny] = 1
                stack.append((nx, ny))
    return True


count1 = 0
for i in range(N):
    for j in range(M):
        if dfs1(i, j):
            count1 += 1

count2 = 0
for i in range(N):
    for j in range(M):
        if dfs2(i, j):
            count2 += 1

print(count1, count2)