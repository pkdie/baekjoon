n = int(input())
score = []
result = 0
for _ in range(n):
    score.append(int(input()))

max_score = score[-1]
for i in range(len(score) - 2, -1, -1):
    if score[i] > max_score:
        result += score[i] - (max_score - 1)
        max_score -= 1
        continue

    if score[i] < max_score:
        max_score = score[i]
        continue

    if score[i] == max_score:
        result += 1
        max_score = max_score - 1
        continue

print(result)