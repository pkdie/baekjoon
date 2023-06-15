n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()

ans = []


def dfs(x):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in range(x, n):
        ans.append(seq[i])
        dfs(i)
        ans.pop()

dfs(0)