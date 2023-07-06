n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
result = []

for i in range(n):
    result.append(rope[i] * (i + 1))

print(max(result))