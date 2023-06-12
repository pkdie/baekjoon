n, s = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0

subseq = []

def dfs(start):
    global cnt
    if sum(subseq) == s and len(subseq) > 0:
        cnt += 1

    for i in range(start, n):
        subseq.append(seq[i])
        dfs(i + 1)
        subseq.pop()

dfs(0)
print(cnt)