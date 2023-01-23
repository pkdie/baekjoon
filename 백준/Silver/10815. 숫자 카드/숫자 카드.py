import sys

N = int(sys.stdin.readline())
ownedcard = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
dic = {}
for i in range(len(ownedcard)):
    dic[ownedcard[i]] = 0
for num in card:
    if num in dic.keys():
        print(1, end=" ")
    else:
        print(0, end=" ")