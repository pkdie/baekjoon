n, m = map(int ,input().split())
seq = sorted(list(map(int, input().split())))
ans = []

def dfs(x):
    if len(ans) == m:
        print(*ans)
        return
    remember_me = 0
    for i in range(x, n):
        if seq[i] != remember_me:

            ans.append(seq[i])
            remember_me = seq[i]
            dfs(i + 1)
            ans.pop()

dfs(0)