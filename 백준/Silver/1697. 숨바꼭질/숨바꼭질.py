from collections import deque

N, K = map(int, input().split()) # N은 수빈이가 있는 위치, K는 동생이 있는 위치

graph = [0] * 100001

dx = [-1, 1]

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()
    for i in range(3):
        if i == 2:
            nx = 2 * x
        else:
            nx = x + dx[i]

        if nx < 0 or nx >= 100001 or nx == N:
            continue
        if graph[nx] == 0:
            graph[nx] = graph[x] + 1
            queue.append(nx)

print(graph[K])