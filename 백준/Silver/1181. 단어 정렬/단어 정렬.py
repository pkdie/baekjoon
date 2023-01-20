import sys

N = int(sys.stdin.readline())
words = []

for _ in range(N):
    word = sys.stdin.readline().strip()
    words.append(word)
words = list(set(words))
words.sort()
words.sort(key=lambda x: len(x))
for word in words:
    print(word)