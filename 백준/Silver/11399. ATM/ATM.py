n = int(input())
time = list(map(int, input().split()))
time.sort()

waiting = 0
sum = 0
for t in time:
    sum += waiting + t
    waiting += t

print(sum)