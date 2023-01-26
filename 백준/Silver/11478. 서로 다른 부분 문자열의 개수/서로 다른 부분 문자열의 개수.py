import sys

S = list(sys.stdin.readline().strip())
result = set()
for i in range(len(S)):
    char = S[i]
    result.add(char)
    while i + 1 <= len(S) - 1:
        char += S[i + 1]
        result.add(char)
        i += 1
print(len(result))