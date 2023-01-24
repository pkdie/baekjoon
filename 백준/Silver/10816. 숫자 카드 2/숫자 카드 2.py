import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
candidate = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1


for candid in candidate:
    cnt = count.get(candid)
    print(cnt if type(cnt) == int else 0, end=" ")