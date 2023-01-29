import sys

S = sys.stdin.readline()
alphabet = [chr(i) for i in range(97, 123)]
cnt = [0 for _ in range(ord("a"), ord("z") + 1)]
for spell in S:
    for i in alphabet:
        if spell == i:
            cnt[alphabet.index(i)] += 1
            break
for i in cnt:
    print(i, end=" ")