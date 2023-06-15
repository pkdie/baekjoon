n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()

ans = []

def dfs():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for num in seq:
        ans.append(num)
        dfs()
        ans.pop()

dfs()