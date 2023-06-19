n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
visited = [False] * n

ans = []


def dfs():
    if len(ans) == m:
        print(*ans)
        return
    remember_me = 0
    for i in range(0, n):
        if not visited[i] and remember_me != seq[i]:
            ans.append(seq[i])
            visited[i] = True
            remember_me = seq[i]
            dfs()
            ans.pop()
            visited[i] = False

dfs()