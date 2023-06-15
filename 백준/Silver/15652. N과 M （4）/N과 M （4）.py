n, m = map(int, input().split())
ans = []

def dfs(x):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in range(x, n + 1):
        ans.append(i)
        dfs(i)
        ans.pop()

dfs(1)