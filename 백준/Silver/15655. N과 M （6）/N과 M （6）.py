n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
ans = []

def dfs(x):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in range(x, len(seq)):
        if seq[i] not in ans:
            ans.append(seq[i])
            dfs(i + 1)
            ans.pop()

dfs(0)